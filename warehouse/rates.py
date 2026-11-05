"""Shipping rate calculations."""

_EXPRESS_SURCHARGE = 7.0
_VALID_SERVICES = {"standard", "express"}


def shipping_quote(weight_kg: float, zone: str, service: str = "standard") -> float:
    """Quote shipping in dollars.

    Args:
        weight_kg: Shipment weight; must be positive.
        zone: Delivery zone — ``"local"`` or ``"regional"``.
        service: ``"standard"`` (default) or ``"express"``.
            Express adds $7 to the standard rate.

    Returns:
        Quote in dollars, rounded to two decimal places.

    Raises:
        ValueError: On invalid weight, zone, or service.
    """
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    if zone not in {"local", "regional"}:
        raise ValueError("unknown zone")
    if service not in _VALID_SERVICES:
        raise ValueError(f"unknown service: {service!r}")
    base = 5.0 if zone == "local" else 8.0
    surcharge = _EXPRESS_SURCHARGE if service == "express" else 0.0
    return round(base + 1.5 * weight_kg + surcharge, 2)
