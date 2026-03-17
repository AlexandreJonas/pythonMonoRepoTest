from pydantic import BaseModel

class importClass(BaseModel):
    nome: str
    desc: str | None = None
    taxinha: float
    sla: float | None = None