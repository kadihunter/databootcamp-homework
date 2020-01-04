
-- List Employee information - employee #, Last name, First Name, Gender and Salary - complete an inner join to allow salary information to flow from separate table

SELECT employeeinformation.employeenum, employeeinformation.lastname, employeeinformation.firstname, employeeinformation.gender, salaries.salary  
from EmployeeInformation
INNER JOIN salaries ON
employeeinformation.employeenum = salaries.employeenum

-- List all employees hired in 1986

SELECT lastname, firstname, hiredate
from EmployeeInformation
WHERE hiredate between '1986-01-01' and '1986-12-31'


--List managers for each department - department#, department name, manager employee number, last name, first name, start and end dates --

SELECT
managerdepartments.departmentnum,
departments.departmentname,
managerdepartments.employeenum,
employeeinformation.lastname,
employeeinformation.firstname,
employeeinformation.hiredate,
employeedepartments.dependdate
from managerdepartments
JOIN employeeinformation ON
managerdepartments.employeenum = employeeinformation.employeenum
JOIN employeedepartments ON
managerdepartments.employeenum = employeedepartments.employeenum
JOIN departments ON
managerdepartments.departmentnum = departments.departmentnum
ORDER by departmentnum

--List department of each employee - employee#, last name, first name, department name

SELECT employeeinformation.employeenum,
employeeinformation.firstname,
employeeinformation.lastname,
departments.departmentname
from employeeinformation
FULL JOIN employeedepartments ON 
employeeinformation.employeenum = employeedepartments.employeenum 
JOIN departments ON
employeedepartments.departmentnum = departments.departmentnum
ORDER by employeenum

--List all employees who first name is "Hercules" and last name begins with "B"

SELECT firstname, lastname
from employeeinformation
where firstname = 'Hercules' AND lastname LIKE 'B%'

--List all employees in Sales - employee#, last name, first name, department name

SELECT employeeinformation.employeenum,
employeeinformation.firstname,
employeeinformation.lastname,
departments.departmentname
from employeeinformation
FULL JOIN employeedepartments ON 
employeeinformation.employeenum = employeedepartments.employeenum 
JOIN departments ON
employeedepartments.departmentnum = departments.departmentnum
where departmentname = 'Sales'
ORDER by employeenum

--List all employees in Sales & Development - employee#, last name, first name, department name

SELECT employeeinformation.employeenum,
employeeinformation.firstname,
employeeinformation.lastname,
departments.departmentname
from employeeinformation
FULL JOIN employeedepartments ON 
employeeinformation.employeenum = employeedepartments.employeenum 
JOIN departments ON
employeedepartments.departmentnum = departments.departmentnum
where departmentname = 'Sales'
ORDER by employeenum

--In Descending order list the frequency count of employees last names

SELECT lastname, count(lastname) AS "Frequency"
from employeeinformation
Group by lastname
ORDER by 2 DESC
