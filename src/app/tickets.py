from src.config import Config
import logging
from src.app.logger import Logger
from redminelib import Redmine
from datetime import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import os


class Tickets:
    """
    Takes opened tickets under specific project on redmine.
    """

    def __init__(self):
        """
        Constructer function.
        Gets some information from config file.
        :return: None.
        """
        self.projects = Config.PROJECTS
        self.url = Config.URL
        self.username = Config.USERNAME
        self.password = Config.PASSWORD
        self.start_date = Config.START_DATE
        self.log_dir = Config.LOG_DIR
        self.times_file_prefix = Config.TIMES_FILE_PREFIX
        self.times_file_suffix = Config.TIMES_FILE_SUFFIX
        self.logger = Logger('Tickets')

    def get_tickets(self):
        try:
            """
            last_read_time = self.get_last_read_time()
            if last_read_time != "":
                self.start_date = last_read_time
            """
            end_date = datetime.today().strftime('%Y-%m-%dT%H:%M:%SZ')
            redmine = Redmine(self.url, username=self.username, password=self.password, requests={'verify': False})
            for project in self.projects:
                project_id = self.get_project_id(redmine, project)
                if project_id != -1:
                    tickets = redmine.issue.filter(project_id=project_id, created_on="><{}|{}".format(self.start_date, end_date), status_id='*')
                    for ticket in tickets:
                        project_name = ticket.project.name if hasattr(ticket, "project") else ""
                        ticket_id = ticket.id if hasattr(ticket, "id") else ""
                        tracker = ticket.tracker.name if hasattr(ticket, "tracker") else ""
                        status = ticket.status.name if hasattr(ticket, "status") else ""
                        priority = ticket.priority.name if hasattr(ticket, "priority") else ""
                        author = ticket.author.name if hasattr(ticket, "author") else ""
                        assigned_to = ticket.assigned_to if hasattr(ticket, "assigned_to") else ""
                        category = ticket.category.name if hasattr(ticket, "category") else ""
                        created_on = ticket.created_on if hasattr(ticket, "created_on") else ""
                        updated_on = ticket.updated_on if hasattr(ticket, "updated_on") else ""
                        self.logger.log(logging.INFO, "project={}$$ticket_id={}$$tracker={}$$status={}$$priority={}$$author={}$$assigned_to={}$$category={}$$created_on={}$$updated_on={}"
                        .format(project_name, ticket_id, tracker, status, priority, author, assigned_to, category, created_on, updated_on))
                        #print(list(ticket))
            #self.set_last_read_time(end_date)
        except Exception as e:
            self.logger.log(logging.WARNING, "Error while getting ticket from redmine")
            self.logger.log(logging.ERROR, e)

    def get_project_id(self, redmine, project_name):
        try:
            projects = redmine.project.all()
            for project in projects:
                if project.name == project_name:
                    return project.id
            else:
                return -1
        except Exception as e:
            self.logger.log(logging.WARNING, "Error while getting project id from redmine")
            self.logger.log(logging.ERROR, e)

    """
    def get_last_read_time(self):
        try:
            date = datetime.today().strftime('%Y-%m-%d')
            file = self.log_dir + self.times_file_prefix + "_" + date + self.times_file_suffix
            if os.path.exists(file):
                with open(file, "r") as f1:
                    lines = f1.readlines()
                    if len(lines) > 0:
                        return lines[-1].rstrip('\n')
                    else:
                        return ""
            else:
                return ""
        except Exception as e:
            self.logger.log(logging.WARNING, "Error while getting last read time from file")
            self.logger.log(logging.ERROR, e)

    def set_last_read_time(self, end_date):
        try:
            date = datetime.today().strftime('%Y-%m-%d')
            file = self.log_dir + self.times_file_prefix + "-" + date + self.times_file_suffix
            with open(file, "a+") as f1:
                f1.write(end_date + "\n")
        except Exception as e:
            self.logger.log(logging.WARNING, "Error while setting last read time to file")
            self.logger.log(logging.ERROR, e)
    """