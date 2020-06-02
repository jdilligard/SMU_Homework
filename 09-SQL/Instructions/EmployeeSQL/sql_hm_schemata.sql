-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/sVKqJZ
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "departments" (
    "dept_no" VARCHAR(8)   NOT NULL,
    "dept_name" VARCHAR(50)   NOT NULL,
    "dept_id" SERIAL   NOT NULL,
    "last_updated" timestamp   NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "pk_departments" PRIMARY KEY (
        "dept_id"
     )
);

CREATE TABLE "dept_emp" (
    "dept_emp_id" SERIAL   NOT NULL,
    "emp_no" INT   NOT NULL,
    "dept_no" VARCHAR(8)   NOT NULL,
    "last_updated" timestamp   NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "pk_dept_emp" PRIMARY KEY (
        "dept_emp_id"
     )
);

CREATE TABLE "dept_manager" (
    "dept_no" VARCHAR(8)   NOT NULL,
    "emp_no" INT   NOT NULL,
    "dept_man_id" SERIAl   NOT NULL,
    "last_updated" timestamp   NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "pk_dept_manager" PRIMARY KEY (
        "dept_man_id"
     )
);

CREATE TABLE "employees" (
    "emp_no" INT   NOT NULL,
    "emp_title_id" VARCHAR(12)   NOT NULL,
    "birth_date" VARCHAR(15)   NOT NULL,
    "first_name" VARCHAR(30)   NOT NULL,
    "last_name" VARCHAR(50)   NOT NULL,
    "sex" VARCHAR(5)   NOT NULL,
    "hire_date" VARCHAR(15)   NOT NULL,
    "last_updated" timestamp   NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "pk_employees" PRIMARY KEY (
        "emp_no"
     )
);

CREATE TABLE "salaries" (
    "emp_no" INT   NOT NULL,
    "salary" INT   NOT NULL,
    "salary_id" SERIAL   NOT NULL,
    "last_updated" timestamp   NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "pk_salaries" PRIMARY KEY (
        "salary_id"
     )
);

CREATE TABLE "titles" (
    "emp_title_id" VARCHAR(12)   NOT NULL,
    "title" VARCHAR(50)   NOT NULL,
    "last_updated" timestamp   NULL DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE "departments" ADD CONSTRAINT "fk_departments_dept_no" FOREIGN KEY("dept_no")
REFERENCES "dept_emp" ("dept_no");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_dept_no" FOREIGN KEY("dept_no")
REFERENCES "departments" ("dept_no");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "employees" ADD CONSTRAINT "fk_employees_emp_no" FOREIGN KEY("emp_no")
REFERENCES "dept_emp" ("emp_no");

ALTER TABLE "employees" ADD CONSTRAINT "fk_employees_emp_title_id" FOREIGN KEY("emp_title_id")
REFERENCES "titles" ("emp_title_id");

ALTER TABLE "salaries" ADD CONSTRAINT "fk_salaries_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");



