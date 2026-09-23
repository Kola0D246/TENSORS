# 🗄️ Data Schema

## 🌐 Universal Constraint

> All user-defined fields of two distinct rows in a table **cannot have the same value simultaneously**.

## 🌐 Data type used

1. key -> datatype for primary and foreign key. can be int or hexdec, but must be same across database
2. int -> integer
3. String -> string
4. encrypted -> password, sensitive data
5. enum -> has selected values only
6. timestamp -> full date time YYYY-MM-DD HH:MM:SS
7. time (hh:mm) -> hour:min

---

## 🏢 Site Data — Global

### 1. Login Credential

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| user_id | int | not null | System | Primary key, random, fixed size |
| login_id | String | not null | User | institute email id |
| password | encrypted | not null | User | Hashed + Salted |
| institute_id | int | not null | User | Foreign key, fixed size |
| role | enum | not null | User | Management, HOD, Faculty, Student |
| token_id | String | not null | System | login token |
| created_at | timestamp | not null | System | Time of account creation, constant |
| last_login | timestamp | not null | System | Updated every login (for audit/security) |

---

### 2. Institute Table

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| institute_id | int | not null | System | Primary key, random, fixed size |
| name | String | not null | User | — |
| affiliation | String | not null | User | — |
| location | String | not null | User | — |
| official_communication | String | not null | User | Contact method for institute |
| institute_access_table_id | int | not null | User | — |

---

## 🏫 Data Given by College Management (Admin) — Institute Specific

---

### 1. TimeSlot

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| timeslot_id | int | not null | System | Primary key |
| day | String | not null | User | — |
| period_num | int | not null | User | — |
| start_time | time (hh:mm) | not null | User | — |
| end_time | time (hh:mm) | not null | User | — |

---

### 2. Infra Table (Classrooms / Labs)

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| room_id | int | not null | System | Primary key, redex |
| building_name | not null | user | building_id |
| room_num | str | not null | User | room num or lab name |
| type | enum | not null | User | `Class` (theory), `Lab` (practical) |
| capacity | int | not null | User | Maximum seating capacity |

NOTE: unique(building name, room_num)
---

### 3. Departments Information

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| department_id | int | not null | System | Primary key, redex |
| department_name | String | not null | User | — |

---

### 4. Faculty Table

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| faculty_id | int | not null | System | Primary key, redex |
| faculty_name | String | not null | User | — |
| qualification | String | not null | User | - |


### 5. Course Table

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| course_id | int | not null | System | Primary key, redex |
| course_name | String | not null | User | — |
| course_type | dropdown | not null | User | `major` / `elective` |
| enrolled_students | int | not null | User | — |
| department_id | str | not null | User | Foreign key, M:1 |

---

### 6. Subject Table (One for Each Major/Minor Course)

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| subject_id | int | not null | System | Primary key, redex |
| subject_name | String | not null | User | — |
| course_id | str | not null | User | Foreign key, M:1 |
| total_theory_hours | int | not null | User | — |
| total_practical_hour | int | not null | User | — |

---

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
| subject_id | int | not null | User | Foreign key |

### 3. Faculty - Department (M:M)

NOTE: each faculty is assign for what department

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| faculty_id | int | not null | User | Foreign key |
| department_id | int | not null | User | Foreign key |

### 4.  Faculty - Subject (M:M)

NOTE: each faculty is assign for what subject

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| faculty_id | int | not null | User | Foreign key |
| subject_id | int | not null | User | Foreign key |

### 5. Faculty Unavailability Table

NOTE: faculty is unavailable

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| faculty_id | int | not null | System | Foreign key |
| timeslot_id | int | not null | User | — |
| reason | String | — | User | Reason for unavailability |

---

## OUTPUT TABLE

### Occupancy Table (Actual Timetable)

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| event_id | int | not null | System | Primary key, count |
| room_id | int | not null | AI | Foreign key, default primary sorting |
| timeslot_id | int | not null | AI | Foreign key, default secondary sorting |
| subject_id | int | not null | AI | Foreign key |
| faculty_id | int | not null | AI | Foreign key |
| student_group_id | int | not null | AI | Foreign key |
| status | dropdown | not null | System | `available` / `booked` / `blocked` (e.g., maintenance) |  

NOTE: how we implement icremental changes and backtracking. remove status

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
- dropdown values must be validated at insertion.
- Foreign keys maintain referential integrity across tables.
- Time-related fields use UTC timestamps for consistency.
