from datetime import datetime

class Task:
    def __init__(self, tId, title, startDate, endDate, description):
        self._taskId: int = tId
        self._title: str = title
        self._startDate: datetime = startDate
        self._endDate: datetime = endDate
        self._description: str = description

    @property
    def taskId(self) -> int:
        return self._taskId
    
    @taskId.setter
    def taskId(self, tId: int) -> None:
        rself._taskId = tId

    @property
    def title(self) -> str:
        return self._title
    
    @title.setter
    def title(self, title: str) -> None:
        self._title = title

    #TODO: getter and setters


    


