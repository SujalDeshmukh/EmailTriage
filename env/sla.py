# env/sla.py
# Reward decays the longer an urgent email sits unactioned

def sla_multiplier(sla_minutes: int, step_number: int, steps_per_minute: float = 10.0) -> float:
    """
    Returns a multiplier (0.1 to 1.0) based on how many steps have passed
    relative to the SLA window. More steps = more decay for urgent emails.
    """
    if sla_minutes is None:
        return 1.0  # no SLA = no penalty

    elapsed_minutes = step_number / steps_per_minute
    ratio = elapsed_minutes / sla_minutes

    if ratio <= 0.5:
        return 1.0       # well within SLA — full reward
    elif ratio <= 1.0:
        return 0.7       # approaching SLA — moderate penalty
    elif ratio <= 1.5:
        return 0.4       # SLA breached — heavy penalty
    else:
        return 0.1       # badly overdue — near-zero reward