# Odoo Practice Implementations (Odoo 18/19)

![Odoo](https://img.shields.io/badge/Odoo-18.0%20%7C%2019.0-purple) ![Modules](https://img.shields.io/badge/Modules-5-blue) ![License](https://img.shields.io/badge/License-LGPL--3-green)

> ⭐ **Hospital Management System = built from scratch** — baaki modules practice playgrounds for specific features.

A set of practice implementations built while mastering **Odoo development fundamentals** — models, security ACLs, sequences, wizards, chatter inheritance, QWeb reports and portals. The **Hospital Management System** was built **completely from scratch** (full SDLC); the others exercise specific feature areas.

```
odoo-practice-projects/
├── hospital_pms/          # Odoo 18 hospital PMS application (patients, doctors, appointments)
├── doctor_appoinment/     # Odoo 18 doctor/patient/appointment module (wizard + QWeb PDF reports)
├── patient_management/    # Odoo 18 patient records + reports
├── stock_manage/          # Odoo 19 material stock record keeping
└── task_manegment/        # Odoo 19 to-do/task tracker
```

## What each covers

- **Hospital PMS (⭐ from scratch)** — application-level patient & doctor management with appointment views, sequences and master data. Built end-to-end: model → security → views → reports.
- **Doctor Appointment** — multi-module `hospital_doctor`, `patient`, `appointment` models, sequences, appointment **wizards** (e.g. cancel-appointment flow), and **QWeb reports** (appointment details, receipt, doctor card, paper format).
- **Patient Management** — patient records with `hospital_patient.py`, reports and paper-formats.
- **Stock Manage (SMS)** — record-keeping of material stocks with chatter (`mail`) integration.
- **Task Management** — a simple to-do manager demonstrating basic model/view/state patterns.

## Learning outcomes

- `ir.model.access.csv` security design, record rules & groups
- Sequences (`ir.sequence`) & data files
- Wizards (`TransientModel`) + form inheritance
- QWeb report templates & custom paper-formats
- Website portal basics (patients/portal flows in practice variants)

## License

LGPL-3 (as declared in module manifests).
