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

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass

    def read(self, path: str):
        with open(path, 'r') as file:
            read_data = csv.DictReader(file)
            self.jobs_list = list(read_data)
