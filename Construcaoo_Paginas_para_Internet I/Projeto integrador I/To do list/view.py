from model import app,tasks,Task,BaseModel

class Taskdal(BaseModel):
    @classmethod
    @app.post('/cad')
    def cad(name):
        id=int(len(tasks))
        newtask=Task(id=id,name=name)
        tasks.append(newtask)
    @classmethod
    @app.post('/show')
    def show():
        return(tasks)
    @classmethod
    @app.post('/altertask')
    def altertask(name,newname):
        for i in tasks:
            if i.name==name:
                i.name=newname
        return(tasks)
    @classmethod
    @app.post('/status')
    def status(name):
        for i in tasks:
            if i.name==name:
                i.status="Concluido"
    @classmethod
    @app.post('/apagar')
    def status(name):
        for i in tasks:
            if i.name==name:
                tasks.remove(i)
            



            


