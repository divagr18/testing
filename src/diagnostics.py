from dataclasses import dataclass


@dataclass(frozen=True)
class RetryDiagnostic:
    operation: str
    attempts: int
    final_error: str

    def summary(self) -> str:
        return f"{self.operation} failed after {self.attempts} attempts: {self.final_error}"
