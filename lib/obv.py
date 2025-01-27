# -*- coding: utf-8 -*-
from .utils import get_offset, signed_series, verify_series

def obv(close, volume, offset=None, **kwargs):
    """Indicator: On Balance Volume (OBV)"""
    # Validate arguments
    close = verify_series(close)
    volume = verify_series(volume)
    offset = get_offset(offset)

    # Calculate Result
    signed_volume = signed_series(close, initial=1) * volume
    obv = signed_volume.cumsum()

    # Offset
    if offset != 0:
        obv = obv.shift(offset)

    # Handle fills
    if 'fillna' in kwargs:
        obv.fillna(kwargs['fillna'], inplace=True)
    if 'fill_method' in kwargs:
        obv.fillna(method=kwargs['fill_method'], inplace=True)

    # Name and Categorize it
    obv.name = "OBV"
    obv.category = 'volume'

    return obv



obv.__doc__ = \
"""On Balance Volume (OBV)

On Balance Volume is a cumulative indicator to measure buying and selling
pressure.

Sources:
    https://www.tradingview.com/wiki/On_Balance_Volume_(OBV)
    https://www.tradingtechnologies.com/help/x-study/technical-indicator-definitions/on-balance-volume-obv/
    https://www.motivewave.com/studies/on_balance_volume.htm

Calculation:
    signed_volume = signed_series(close, initial=1) * volume
    obv = signed_volume.cumsum()

Args:
    close (pd.Series): Series of 'close's
    volume (pd.Series): Series of 'volume's
    offset (int): How many periods to offset the result.  Default: 0

Kwargs:
    fillna (value, optional): pd.DataFrame.fillna(value)
    fill_method (value, optional): Type of fill method

Returns:
    pd.Series: New feature generated.
"""