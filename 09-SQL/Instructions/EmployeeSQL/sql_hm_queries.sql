
--THESE ARE MY QUERIES 1 - 8
--Number 1
SELECT 
	*
FROM
	employees em
	join salaries s on em.emp_no = s.emp_no
LIMIT 10;

--Number 2 
SELECT 
	first_name,
	last_name,
	hire_date
FROM
	employees
WHERE 
    hire_date LIKE '%1986';

--Number 3 
SELECT
	de.dept_no,
	de.dept_name,
	e.emp_no,
	e.last_name,
	e.first_name
	
FROM
	dept_manager dm
	join departments de on dm.dept_no = de.dept_no
	join employees e  on dm.emp_no = e.emp_no
	
ORDER BY
	dept_name desc;


--Number 4
SELECT 
	dp.emp_no,
	e.last_name,
	e.first_name,
	de.dept_name
FROM
	dept_emp dp
	join departments de on de.dept_no = dp.dept_no
	join employees e on e.emp_no = dp.emp_no
LIMIT 10;

--Number 5 
SELECT 
	first_name,
	last_name,
	sex
FROM
	employees
WHERE 
    first_name = 'Hercules'
AND
	last_name LIKE 'B%';
	

	
--Number 6 
SELECT 
	dp.emp_no,
	e.last_name,
	e.first_name,
	de.dept_name
FROM
	dept_emp dp
	join departments de on de.dept_no = dp.dept_no
	join employees e on e.emp_no = dp.emp_no
WHERE 
	de.dept_name = 'Sales'
	


--Number 7 
SELECT 
	dp.emp_no,
	e.last_name,
	e.first_name,
	de.dept_name
FROM
	dept_emp dp
	join departments de on de.dept_no = dp.dept_no
	join employees e on e.emp_no = dp.emp_no
WHERE 
	de.dept_name = 'Sales'
OR
	de.dept_name = 'Development'

	
--Number 8 
SELECT 
	last_name,
	count(last_name) as "numwlast"
FROM
	employees
GROUP BY 
	last_name
ORDER BY
	numwlast desc;