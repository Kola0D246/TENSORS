# 🗄️ Data Schema

## 🌐 Data type used

1. int -> integer
2. string -> string
3. hashed -> password, sensitive data
4. enum -> has selected values only
5. timestamp -> full date time YYYY-MM-DD HH:MM:SS
6. time (hh:mm) -> hour:min

---

## 🏢 Site Data — Global

### 1. Login Credential

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| login_id | string | not null, unique | User | Primary key, institute email id |
| password | hashed | not null | User | Hashed + Salted |
| institute_id* | int | not null | User | Foreign key |
| role | enum | not null | User | Management, HOD, Faculty, Student |
| created_at | timestamp | not null | System | Time of account creation, constant |

*NOTE: institute_id is only for multiple institute setup
---

### 2. Session Table

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| token_id | string | not null | System | primary key, random UUID |
| login_id | string | not null, unique | User | Foreign key |
| last_login | timestamp | not null | System | Updated every login (for audit/security) |

NOTE: unique login id means one login_id can be active at only single device at a time

---

## 🏫 Data Given by College Management

---

### 2. Institute Table

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| institute_id | int | not null | System | Primary key, auto_increment |
| institute_name | string | not null | User | — |
| affiliation | string | not null | User | — |
| location | string | not null | User | — |
| contact_info | string | not null | User | Official email |
| email_domain | string | not null | User | for auth verification |

NOTE : If made for single college, this information will be setup as json file

---

### 1. TimeSlot

| Field | Data Type | Constraint | Value By | Remark |
|-------|-----------|------------|----------|--------|
| timeslot_id | int | not null | System | Primary key, auto_increment |
| day | enum | not null | User | working days |
| period_num | int | not null | User | — |

---

### 2. Period time 

| Field | Data Type | Constraint | Value By | Remark |
|-------|-----------|------------|----------|--------|
| period_num | int | not null | User | Primary key |
| start_time | time (hh:mm) | not null | User | — |
| end_time | time (hh:mm) | not null | User | — |

---

### 2. Building Table

| Field | Data Type | Constraint | Value By | Remark |
|-------|-----------|------------|----------|--------|
| building_id | int | not null | System | Primary key, auto_increment |
| building_name | string | not null | User | - |

### 2. Room Table (Classrooms / Labs)

| Field | Data Type | Constraint | Value By | Remark |
|-------|-----------|------------|----------|--------|
| room_id | int | not null | System | Primary key, auto_increment |
| building_id | int | not null | User | Foreign key, M:1 |
| room_num | string | not null | User | room num or lab name |
| room_type | enum | not null | User | `Class` (theory), `smart class` (projector), `Lab` |
| capacity | int | not null | User | Maximum seating capacity |

NOTE: unique(building name, room_num)
NOTE: Building table and building_id only exist if college opt for multiple building

---

### 3. Departments Information

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| department_id | int | not null | System | Primary key, auto_increment |
| department_name | string | not null | User | — |

---

### 4. Faculty Table

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| employee_id | string | not null | User | Primary key |
| faculty_name | string | not null | User | — |
| qualification | string | not null | User | - |


### 5. Course Table

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| course_id | int | not null | System | Primary key, auto_increment |
| course_name | string | not null | User | — |
| course_type | enum | not null | User | `major` / `minor` / `elective` |
| department_id | int | not null | User | Foreign key, M:1 |

NOTE: Adjust for minor courses
NOTE: Should we add semester feild also?
NOTE: Check if same course can be on different department (making M:M relation)

---

### 6. Subject Table

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| subject_code | string | not null | User | Primary key |
| subject_name | string | not null | User | — |
| course_id | int | not null | User | Foreign key, M:1 |
| total_theory_hours | int | not null | User | — |
| total_practical_hour | int | not null | User | — |

---

### 7. Faculty Unavailability Table

NOTE: faculty is unavailable

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| employee_id | string | not null | User | Foreign key |
| timeslot_id | int | not null | User | — |
| reason | string | — | User | Reason for unavailability |

---

### 8. Student Table 

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| enrollment_no | string | not null | User | Primary key |
| student_name | string | not null | User | — |
| department_id | int | not null | User | Foreign key, M:1 |
| semester | enum(int) | not null | User | - |

NOTE: Connect student, faculty with user table.

## RELATIONSHIP TABLE

### 1. Room - Department (M:M)

NOTE: if room are divided between department

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| room_id | int | not null | User | Foreign key |
| department_id | int | not null | User | Foreign key |

### 2. Subject - Lab (M:M)

NOTE: each lab / class is assign for what subjects

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| room_id | int | not null | User | Foreign key |
| subject_code | string | not null | User | Foreign key |

### 3. Faculty - Department (M:M)

NOTE: each faculty is assign for what department

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| faculty_id | int | not null | User | Foreign key |
| department_id | int | not null | User | Foreign key |
| designation | enum | not null | User | 

### 4.  Faculty - Subject (M:M)

NOTE: each faculty is assign for what subject

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| faculty_id | int | not null | User | Foreign key |
| subject_id | int | not null | User | Foreign key |

NOTE: since we have faculty-subject table, do we also need to have faculty-department table?

### 5. Student Course Table

NOTE: course taken by student

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| enrollment_no | string | not null | User | Foreign key |
| course_id | int | not null | User | Foreign key |

---

## OUTPUT TABLE

### Occupancy Table (Actual Timetable)

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| event_id | int | not null | System | Primary key, auto_increment |
| room_id | int | not null | AI | Foreign key, default primary sorting |
| timeslot_id | int | not null | AI | Foreign key, default secondary sorting |
| subject_id | int | not null | AI | Foreign key |
| faculty_id | int | not null | AI | Foreign key |
| student_group_id | int | not null | AI | Foreign key |

#### 🔒 Constraints

1. `room_id` and `timeslot_id` cannot both be identical for two rows → no duplicate slot-room entries.  
2. If two rows have the same `faculty_id` but different `room_id`, their `timeslot_id` must differ (faculty cannot be in two rooms at once).  
3. Rule #2 also applies to `student_group_id` (a student group can’t attend two classes at once).  
4. `faculty_id` and `student_group_id` must correspond to the same `subject_id`.  
5. If status is `available`, assigning valid `faculty_id`, `student_group_id`, and `subject_id` updates status → `booked`.  
   - Do not update if status is `booked` or `blocked`.  
   - When backtracking = true → reset these fields and revert status to `available`.

---

## 🧩 Notes

- All IDs marked as *System* generated are unique and indexed.
- enum values must be validated at insertion.
- Foreign keys maintain referential integrity across tables.
- Time-related fields use UTC timestamps for consistency.
