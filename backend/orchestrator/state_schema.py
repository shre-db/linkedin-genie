__module_name__ = "state_schema"

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class ProfileBotState(BaseModel):
    # User-level meta
    user_id: Optional[str] = Field(default=None, description="Unique identifier for the user")

    # Raw inputs
    linkedin_data: Optional[Dict[str, Any]] = None
    target_role: Optional[str] = None
    job_description: Optional[str] = None

    # Intermediate outputs
    profile_analysis: Optional[str] = None
    content_rewrites: Optional[str] = None
    job_fit_report: Optional[str] = None
    career_guidance: Optional[str] = None

    # Status flags
    steps_completed: Dict[str, bool] = Field(default_factory=lambda: {
        "analyzed": False,
        "rewritten": False,
        "job_fit_checked": False,
        "career_guided": False
    })