# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **Odoo 18.0 Hospital Patient Management System (PMS)** module. It manages patients, doctors, appointments, and specialty categories.

## Module Structure

```
hospital_pms/
├── __manifest__.py           # Module metadata and dependencies
├── models/                   # Python business logic
│   ├── patients.py          # Patient records (hospital.patients)
│   ├── docters.py           # Doctor records (hospital.docters)
│   ├── apoinment.py         # Appointment records (hospital.apoinment)
│   └── cetegory_type.py     # Master data: specialty categories
├── views/                    # XML UI definitions
│   ├── patients_record_views.xml
│   ├── docters_record_views.xml
│   └── apoinment.xml
├── security/                 # Access control
│   └── ir.model.access.csv
├── sequence/                 # Auto-numbering sequences
│   └── sequence.xml
├── master_data/              # Demo/master data
│   ├── patient_master_data.xml
│   └── docter_master_data.xml
└── static/description/       # Module icon
```

## Key Models

| Model | Technical Name | Purpose |
|-------|---------------|---------|
| Patient | `hospital.patients` | Patient records with disease category |
| Doctor | `hospital.docters` | Doctor records with specialty |
| Appointment | `hospital.apoinment` | Links patients to doctors |
| Specialty Category (Patient) | `sp.category` | Master data for patient problems |
| Specialty Category (Doctor) | `spacle.categorys` | Master data for doctor specialties |

## Development Commands

This is an Odoo module - there are no build/test commands within the module itself. Development requires a running Odoo instance:

```bash
# Install/update module in Odoo (run from Odoo server)
./odoo-bin -c odoo.conf -u hospital_pms

# Install with demo data
./odoo-bin -c odoo.conf -i hospital_pms

# Run with specific database
./odoo-bin -d your_database -u hospital_pms --stop-after-init
```

## Key Patterns

### Sequences
Auto-generated IDs using `ir.sequence`:
- Patients: `P-S/00001` format via `patients.seq.order`
- Doctors: `D-S/00001` format via `docters.seq.order`
- Appointments: `O-R/00001` format via `apoinment.seq.order`

Sequences are assigned in `create()` methods via `@api.model_create_multi`.

### Computed Display Names
Both patients and doctors use computed `_rec_name` fields:
- Patient: `name [problem]` format via `rec_patients` field
- Doctor: `name [specialty]` format via `rec_docters` field

### Active/Inactive Status
Models use boolean `active` field with computed `status_text` for UI display:
- Patient: "Treatment On" / "DisCharge"
- Doctor: "On-Duty" / "Off-Duty"

### Dynamic Domain Filtering
Patient form filters `master_ids` (problems) based on `category_filter`:
```xml
domain="[('datatype', '=', category_filter)]"
```

## Important Notes

- **Typo in model file**: `cetegory_type.py` (should be "category")
- **Duplicate class names**: `SpeciltyCategory` defined twice in `cetegory_type.py` (different `_name` attributes though)
- **Unused import**: `from email.policy import default` in patients.py
- **Field redefinition**: `patients_pic` defined twice in apoinment.py (second one with `related` takes effect)
- **Unused variable**: `apoin` field in apoinment.py appears unused

## File Load Order

The `__manifest__.py` `data` list defines load order - security must come before views:
1. `security/ir.model.access.csv`
2. Views (which may reference models)
3. Sequences (ir.sequence records)
4. Master data (ir.model.records)
