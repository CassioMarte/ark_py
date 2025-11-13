class HttpResponse:
    def __init__(self, status_code: int, body: dict | None = None) -> None:
        self.status_code = status_code
        self.body = body or {}


'''
from typing import Any, Dict, Optional
import json
from datetime import datetime


class HttpResponse:
    def __init__(
        self,
        status_code: int,
        body: Optional[Dict[str, Any]] = None,
        log: Optional[Dict[str, Any]] = None
    ) -> None:
        self.status_code = status_code
        self.body = body or {}
        self.log = log or {
            "timestamp": datetime.utcnow().isoformat(),
            "status_code": status_code,
            "message": "Response created successfully"
        }

    def to_dict(self) -> Dict[str, Any]:
        """Retorna a resposta em formato de dicionário completo"""
        return {
            "status_code": self.status_code,
            "body": self.body,
            "log": self.log
        }

    def to_json(self) -> str:
        """Retorna a resposta como JSON (útil para APIs ou logs em arquivo)"""
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

'''