from sqlalchemy import Column,String, Integer, create_engine, ForeignKey, select
from sqlalchemy.orm import registry,relationship, Session

engine = create_engine('mysql+mysqlconnector://root:hemakesh%40mysql@localhost:3306/projects'
                        ,echo=True)

mapper_registry = registry()
#mapper_registry.metadata

Base = mapper_registry.generate_base()

class Project(Base):
    __tablename__ ='projects'
    project_id = Column(Integer, primary_key=True)
    title = Column(String(length = 50))
    description = Column(String(length = 50))

    def __repr__(self):
        return "<Project(title='{0}', description='{1}')>".format(
            self.title, self.description
        )
    
class Task(Base):
    __tablename__ = "tasks"
    task_id = Column(Integer, primary_key = True)
    project_id = Column(Integer, ForeignKey("projects.project_id"))
    description = Column(String(length = 50))

    project = relationship("Project")

    def __repr__(self):
        return "<Task(description = '{0}'>".format(self.description)
    
Base.metadata.create_all(engine)

# with Session(engine) as session:
#     organize_closet_project = Project(title = "organize closet", description = "organize closet by color and style")

#     session.add(organize_closet_project)

#     session.flush()

#     tasks = [
#         Task(project_id = organize_closet_project.project_id,
#              description = "decide which clothes to donate"),
#         Task(project_id = organize_closet_project.project_id,
#              description = "organise summer clothes"),
#         Task(project_id = organize_closet_project.project_id,
#              description = "organize winter clothes")
#     ]


#     session.bulk_save_objects(tasks)
#     session.commit()

with Session(engine) as session:
    smt = select(Project).where(Project.title == "Organize closet")

    results = session.execute(smt)
    organize_closet_project = results.scalar()

    smt = select(Task).where(Task.project_id == organize_closet_project.project_id)

    results = session.execute(smt)
    for task in results:
        print(task)