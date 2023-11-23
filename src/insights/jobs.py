from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self) -> List[Dict]:
        pass

    def get_unique_job_types(self) -> List[str]:
        jobs = set()
        for job_info in self.jobs_list:
            job_type = job_info.get('job_type')
            jobs.add(job_type)
        return jobs

    def filter_by_multiple_criteria(self, jobs, filter_criteria) -> List[dict]:
        if not isinstance(jobs, list):
            raise TypeError('jobs must be a list')
        if not isinstance(filter_criteria, dict):
            raise TypeError('criteria must be a dict')

        result = list()
        filtered_jobs = list(filter(lambda job: all(job[key] == value for key, value in filter_criteria.items()), jobs))
        return filtered_jobs

    def read(self, path: str):
        with open(path, 'r') as file:
            read_data = csv.DictReader(file)
            self.jobs_list = list(read_data)
