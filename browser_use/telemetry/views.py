from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from typing import Any, Dict, Literal, Optional

from browser_use.controller.registry.views import ActionModel


@dataclass
class BaseTelemetryEvent(ABC):
	@property
	@abstractmethod
	def name(self) -> str:
		pass

	@property
	def properties(self) -> Dict[str, Any]:
		return {k: v for k, v in asdict(self).items() if k != 'name'}


@dataclass
class RegisteredFunction:
	name: str
	params: dict[str, Any]


@dataclass
class ControllerRegisteredFunctionsTelemetryEvent(BaseTelemetryEvent):
	registered_functions: list[RegisteredFunction]
	name: str = 'controller_registered_functions'


@dataclass
class AgentStepTelemetryEvent(BaseTelemetryEvent):
	agent_id: str
	step: int
	consecutive_failures: int
	actions: list[dict]
	version: str
	source: str
	model_name: str
	chat_model_library: str
	step_error: Optional[list[str]] = None
	name: str = 'agent_step'


@dataclass
class AgentTaskTelemetryEvent(BaseTelemetryEvent):
	agent_id: str
	task: str
	task_plan: str
	difficulty: int
	tags: list[str]
	summary: str
	name: str = 'agent_task'


@dataclass
class AgentRunTelemetryEvent(BaseTelemetryEvent):
	agent_id: str
	use_vision: bool
	task: str
	model_name: str
	chat_model_library: str
	version: str
	source: str
	name: str = 'agent_run'


@dataclass
class AgentEndTelemetryEvent(BaseTelemetryEvent):
	agent_id: str
	steps: int
	max_steps_reached: bool
	success: bool
	errors: list[str]
	status: Literal['success', 'failure', 'unknown']
	status_reason: Optional[str] = None
	name: str = 'agent_end'
