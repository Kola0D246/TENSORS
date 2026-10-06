# 🧾 User Input Specification - Smart Classroom and Timetable Scheduler

## 1️⃣ Institute Registration (by Management)

| Field | Type | Required | Description |
|--------|------|-----------|-------------|
| Institute Name | String | ✅ | Name of the college |
| Affiliation | String | ✅ | University or governing body |
| Location | String | ✅ | City, state |
| Institute Contact Info | String | ✅ | Official contact number/email |
| College Email Domain | String | ✅ | Used for admin verification |

---

## 2️⃣ Admin Inputs

| Field | Type | Required | Description |
|--------|------|-----------|-------------|
| Department Name | String | ✅ | Name of department |
| Classroom/Lab Info | Object | ✅ | Room number, type, capacity, department |
| Time Slots | Object | ✅ | Periods, start time, end time |
| Faculty Info | List | ✅ | Name |
| Student Info | List | ✅ | Enrollment no, opted major/minor/electives |


---

## 3️⃣ HOD Inputs

| Field | Type | Required | Description |
|--------|------|-----------|-------------|
| Course info | Objects | ✅ | Course Name, type |
| Subjects | List | ✅ | Subject name, theory/practical hours |

---

## 4️⃣ Faculty Inputs

| Field | Type | Required | Description |
|--------|------|-----------|-------------|
| Unavailability | Schedule | ✅ | Days and times faculty is available |

---

## 🧠 Additional Inputs for Optimization

| Parameter | Description |
|------------|-------------|
| Maximum teaching hours/week | AICTE workload limit |
| Minimum gap between classes | Faculty relaxation constraint |
| Preferred Lab Times | Department-level rules |
| Weightage Settings | Admin chooses optimization priorities (faculty balance vs. room use) |
