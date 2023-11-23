from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def __get_salaries(self, salaryType) -> Union[int, str]:
        salaries = [float(job.get(salaryType)) for job in self.jobs_list if job.get(salaryType).isdigit()]
        return salaries

    def get_max_salary(self) -> int:
        salaries = self.__get_salaries('max_salary')
        return max(salaries, default=0)

    def get_min_salary(self) -> int:
        salaries = self.__get_salaries('min_salary')
        return min(salaries, default=0)

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        min_salary = job.get('min_salary')
        max_salary = job.get('max_salary')

        if min_salary is None or max_salary is None:
            raise ValueError('salary range is not specified')

        try:
            salary = int(salary)
            min_salary = int(min_salary)
            max_salary = int(max_salary)
        except (ValueError, TypeError):
            raise ValueError('salary is not a number')

        if min_salary > max_salary:
            raise ValueError('minimum salary is greater than maximum salary')

        return min_salary <= salary <= max_salary

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
