-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

CREATE TABLE "EmployeeInformation" (
    "EmployeeNum" int   NOT NULL,
    "BirthDate" DATE   NOT NULL,
    "FirstName" VARCHAR   NOT NULL,
    "LastName" VARCHAR   NOT NULL,
    "Gender" VARCHAR   NOT NULL,
    "HireDate" DATE   NOT NULL,
    CONSTRAINT "pk_EmployeeInformation" PRIMARY KEY (
        "EmployeeNum"
     )
);

CREATE TABLE "ManagerDepartments" (
    "DepartmentNum" VARCHAR   NOT NULL,
    "EmployeeNum" int   NOT NULL,
    "FromDate" DATE   NOT NULL,
    "ToDate" DATE   NOT NULL
);

CREATE TABLE "EmployeeDepartments" (
    "EmployeeNum" int   NOT NULL,
    "DepartmentNum" VARCHAR   NOT NULL,
    "DepStartDate" DATE   NOT NULL,
    "DepEndDate" DATE   NOT NULL
);

CREATE TABLE "Departments" (
    "DepartmentNum" VARCHAR   NOT NULL,
    "DepartmentName" VARCHAR   NOT NULL,
    CONSTRAINT "pk_Departments" PRIMARY KEY (
        "DepartmentNum"
     )
);

CREATE TABLE "Titles" (
    "EmployeeNum" int   NOT NULL,
    "Title" VARCHAR   NOT NULL,
    "TitleStartDate" DATE   NOT NULL,
    "TitleEndDate" DATE   NOT NULL
);

CREATE TABLE "Salaries" (
    "EmployeeNum" int   NOT NULL,
    "Salary" int   NOT NULL,
    "SalStartDate" DATE   NOT NULL,
    "SalEndDate" DATE   NOT NULL
);

ALTER TABLE "ManagerDepartments" ADD CONSTRAINT "fk_ManagerDepartments_DepartmentNum" FOREIGN KEY("DepartmentNum")
REFERENCES "Departments" ("DepartmentNum");

ALTER TABLE "ManagerDepartments" ADD CONSTRAINT "fk_ManagerDepartments_EmployeeNum" FOREIGN KEY("EmployeeNum")
REFERENCES "EmployeeInformation" ("EmployeeNum");

ALTER TABLE "EmployeeDepartments" ADD CONSTRAINT "fk_EmployeeDepartments_EmployeeNum" FOREIGN KEY("EmployeeNum")
REFERENCES "EmployeeInformation" ("EmployeeNum");

ALTER TABLE "EmployeeDepartments" ADD CONSTRAINT "fk_EmployeeDepartments_DepartmentNum" FOREIGN KEY("DepartmentNum")
REFERENCES "Departments" ("DepartmentNum");

ALTER TABLE "Titles" ADD CONSTRAINT "fk_Titles_EmployeeNum" FOREIGN KEY("EmployeeNum")
REFERENCES "EmployeeInformation" ("EmployeeNum");

ALTER TABLE "Salaries" ADD CONSTRAINT "fk_Salaries_EmployeeNum" FOREIGN KEY("EmployeeNum")
REFERENCES "EmployeeInformation" ("EmployeeNum");