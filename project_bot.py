import json


class project_goblin:
    def __init__(self):
        self.projects_in_progress = []
        self.week_counter = 0
        self.projects_completed = []
        
        try:
            self.project_fp = open("data/project_data.json", "r+")
        except IOError:
            self.project_fp = open("data/project_data.json", "w")
            self.project_fp.close()
            self.project_fp = open("data/project_data.json", "r+")
            
 
        try:
            self.projects_in_progress = json.load(self.project_fp)
            print("Valid project_data file found")
        except:
            print("No valid project_data file found, will be created on shutdown")
            
            
            
            
            
        try:
            self.completed_fp = open("data/completed_data.json", "r+")
        except IOError:
            self.completed_fp = open("data/completed_data.json", "w")
            self.completed_fp.close()
            self.completed_fp = open("data/completed_data.json", "r+")
            
 
        try:
            self.projects_completed = json.load(self.completed_fp)
            print("Valid completed_data file found")
        except:
            print("No valid completed_data file found, will be created on shutdown")
            
            
            
            
        try:
            self.date_fp = open("data/date_data.json", "r+")
        except IOError:
            self.date_fp = open("data/date_data.json", "w")
            self.date_fp.close()
            self.date_fp = open("data/date_data.json", "r+")
            
 
        try:
            self.week_counter = json.load(self.date_fp)
            print("Valid date_data file found")
        except:
            print("No valid date_data file found, will be created on shutdown")    
            
            
            
            
            
        
        
    def __del__(self):
        print("Saving project data...")
        self.project_fp.seek(0)
        self.project_fp.truncate(0)
        
        json.dump(self.projects_in_progress, self.project_fp)
        
        self.project_fp.close()
        
        
        
        
        self.completed_fp.seek(0)
        self.completed_fp.truncate(0)
        
        json.dump(self.projects_completed, self.completed_fp)
        
        self.completed_fp.close()
        
        
        
        
        self.date_fp.seek(0)
        self.date_fp.truncate(0)
        
        json.dump(self.week_counter, self.date_fp)
        
        self.date_fp.close()
        
        
    def create_output(self, text):
        msg = ''
        
        # !G project create /project/ /number of weeks/
        if text[2] == 'create':
            msg = self.create_project(text)
        if text[2] == 'progress':
            msg = self.progress_week()
        if text[2] == 'list':
            msg = self.project_list()
        if text[2] == 'completed':
            msg = self.completed_list()
        if text[2] == 'delete':
            msg = self.delete_project(text)
        if text[2] == 'complete':
            msg = self.complete_project(text)

        return msg
        
    def reset_projects(self):
        msg = 'Projects reset'
        
        self.projects_in_progress = []
        self.week_counter = 0
        self.projects_completed = []

        return msg
    
    def create_project(self, text):
        msg = ''
        
        project = {}
        project["project"] = ''
        project["time"] = 0
        
        # add project fields
        project["name"] = ' '.join(text[3:-1])
        project["time"] = int(text[-1])
        
        self.projects_in_progress.append(project)
        
        print(self.projects_in_progress)
        
        msg += "```Project \""
        msg += project["name"]
        msg += "\" will be completed in "
        msg += str(project["time"])
        msg += " weeks```"
        
        return msg
        # project_name number_of_weeks
        
        
    def progress_week(self):
        # decrement time field by 1
        # announce projects that have reached 0
        # remove from list and add to complete projects
        msg = ''
        msg += '```Week ' + str(self.week_counter)
        msg += ' -> ' + str(self.week_counter + 1)
        msg += '\n'
        
        self.week_counter += 1

        for p in self.projects_in_progress:
            msg += p['name'] + ': Weeks remaining '
            msg += str(p['time']) + ' -> '
            p['time'] -= 1
            msg += str(p['time'])
            msg += '\n'
    
        msg += '\n-----------------------\n'
        msg += 'Projects completed this week:\n'
        for p in self.projects_in_progress:
            if p['time'] == 0:
                msg += p['name']
                msg += '\n'
                
                save_str = '\"' + p['name']
                save_str += '\" finished on Week '
                save_str += str(self.week_counter)
                
                self.projects_completed.append(save_str)
                self.projects_in_progress.remove(p)
                continue
            
        msg += '```'

        return msg
        
    def project_list(self):
        msg = ''
        msg += '```Current projects in progress:\n'
        counter = 0
        
        for p in self.projects_in_progress:
            msg += '' + str(counter) + ': '
            msg += p['name']
            msg += ' [' + str(p['time'])
            msg += ' weeks]\n'
            counter += 1
            
        msg += '```'
        
        return msg
        
    def completed_list(self):
        msg = ''
        msg += '```'
        msg += 'Completed Projects: \n'
        
        for m in self.projects_completed:
            msg += m
            msg += '\n'
            
        msg += '```'
        
        return msg
        
        
    def delete_project(self, text):
        msg = ''
        #!G project delete 0
        msg = '```'
        
        del_num = int(text[3])
        
        counter = 0
        
        for p in self.projects_in_progress: 
            if counter == del_num:
                msg += p['name']
                msg += ' deleted'
                self.projects_in_progress.remove(p)
                break
            counter += 1
        
        msg += '```'
        
        return msg
        
    def complete_project(self, text):
        msg = ''
        #!G project complete 0
        msg = '```'
        
        complete_num = int(text[3])
        
        counter = 0
        for p in self.projects_in_progress:
            if counter == complete_num:
                msg += p['name']
                msg += ' completed!'
                self.projects_in_progress.remove(p)
                
                save_str = '\"' + p['name']
                save_str += '\" finished on Week '
                save_str += str(self.week_counter)
                
                self.projects_completed.append(save_str)
                self.projects_in_progress.remove(p)
                break
            counter += 1
            
        msg += '```'
        
        return msg
        
        
        
        
        
        
        
        
        
        