# Parameter descriptions for function detail pages (UTF-8 via unicode_escape)
from __future__ import annotations

from typing import Dict, List, Tuple

ParamDoc = Tuple[str, str]  # (param_name, description_ko)


def u(s: str) -> str:
    return s.encode("ascii").decode("unicode_escape")


# Shared snippets (category: bootstrap)
_REF_DATE = u("\\uae30\\uc900\\uc77c. \\uace1\\uc120 \\ubd80\\ud2b8\\uc2a4\\ud2b8\\ub7a9 \\ubc0f \\ud560\\uc778 \\uacc4\\uc0b0\\uc758 \\uae30\\uc900 \\ub0a0\\uc9dc (YYYY-MM-DD)")
_CURVE_TYPE = u("\\uace1\\uc120 \\ucee8\\ubca4\\uc158 \\ucf54\\ub4dc (\\uc608: zero_krw_cd). \\uc77c\\uc218\\uacc4\\uc0b0\\u00b7\\uce98\\ub9b0\\ub354\\u00b7\\ubd80\\ud2b8\\uc2a4\\ud2b8\\ub7a9 \\ubc29\\uc2dd\\uc744 \\uc815\\uc758")
_BOND_QUOTE = u("\\ucc44\\uad8c \\uacac\\uc801 \\ud14c\\uc774\\ube14. \\ud5e4\\ub354: tenor, type, quote \\uceec\\ub7fc (type\\uc740 deposite\\u00b7swap\\u00b7bond \\ub4f1)")
_SWAP_QUOTE = u("\\uc2a4\\uc651 \\uacac\\uc801 \\ud14c\\uc774\\ube14. \\ud5e4\\ub354: tenor, type, quote \\uceec\\ub7fc (type\\uc740 deposite\\u00b7swap \\ub4f1)")
_BASIS_QUOTE = u("CCBS \\ubca0\\uc774\\uc2dc\\uc2a4 \\uc2a4\\uc651 \\uacac\\uc801 \\ud14c\\uc774\\ube14. \\ud5e4\\ub354: tenor, type, quote \\uceec\\ub7fc")
_CCFS_QUOTE = u("CCFS \\uace0\\uc815\\uae08\\ub9ac \\uc2a4\\uc651 \\uacac\\uc801 \\ud14c\\uc774\\ube14. \\ud5e4\\ub354: tenor, type, quote \\uceec\\ub7fc")
_DISCOUNT_CURVE = u("\\uc678\\ubd80 \\ud560\\uc778 \\uace1\\uc120 \\ub370\\uc774\\ud130. time/tenor\\u00b7zeroRate \\ub610\\ub294 quote \\ud615\\ud0dc\\uc758 \\uace1\\uc120 \\ud14c\\uc774\\ube14")
_BASE_CURVE = u("\\uae30\\uc900\\ud1b5\\ud654 \\uc778\\ub371\\uc2a4 \\uace1\\uc120 \\ub370\\uc774\\ud130 (time/tenor\\u00b7zeroRate \\ub610\\ub294 quote \\ud14c\\uc774\\ube14)")
_SW_CURVE = u("\\uc785\\ub825 \\uace1\\uc120 \\ub370\\uc774\\ud130. time\\u00b7quote(YTM) \\ub610\\ub294 tenor\\u00b7quote, zeroRate \\uc9c1\\uc811 \\uc785\\ub825\\ub3c4 \\uac00\\ub2a5")
_UFR = u("Ultimate Forward Rate. Smith-Wilson \\uc7a5\\uae30 \\uc218\\ub839 \\uae08\\ub9ac")
_ALPHA = u("Smith-Wilson \\uc218\\ub839 \\uc18d\\ub3c4 \\ud30c\\ub77c\\ubbf8\\ud130 \\u03b1")
_OUT_TIMES = u("\\ucd9c\\ub825 \\ub9cc\\uae30 \\ubaa9\\ub85d (time \\ub610\\ub294 tenor). \\ube44\\uc5b4 \\uc788\\uc73c\\uba74 curveData\\uc758 time \\uc0ac\\uc6a9")
_SPOT_CURVE = u("\\uc5f0\\uc18d\\ubcf5\\ub9ac \\uc2a4\\ud31f(zeroRate) \\uace1\\uc120. time\\u00b7zeroRate \\ub610\\ub294 tenor\\u00b7zeroRate")

# Shared snippets (general)
_CURVE_DATA_ZD = u("\\uace1\\uc120 \\ub370\\uc774\\ud130 (zeroRate \\ub610\\ub294 discount). time/tenor\\u00b7zeroRate \\ub610\\ub294 quote \\ud14c\\uc774\\ube14")
_DATE_OR_TIME = u("\\ubcf4\\uac04\\u00b7\\ucd9c\\ub825 \\ub300\\uc0c1 \\uc77c\\uc790 \\ub610\\ub294 \\ub9cc\\uae30(time/tenor) \\ubaa9\\ub85d")
_VALUE_DATE = u("\\ud3c9\\uac00\\uc77c (YYYY-MM-DD)")
_OUTPUT_TYPE = u("\\ucd9c\\ub825 \\uc720\\ud615. pricing\\u00b7cashflow\\u00b7greeks\\u00b7input_items \\ub4f1")
_NOTIONAL = u("\\uba85\\uc758\\uae08\\uc561")
_MATURITY = u("\\ub9cc\\uae30. \\ub0a0\\uc9dc \\ub610\\ub294 \\ud14c\\ub108 (\\uc608: 10Y)")
_MATURITY_TENOR = u("\\ub9cc\\uae30 \\ud14c\\ub108 (\\uc608: 5Y, 10Y)")
_FIXED_RATE = u("\\uace0\\uc815\\uae08\\ub9ac (\\uc5f0\\uac04 \\ube44\\uc728)")
_ISSUE_DATE = u("\\ubc1c\\ud589\\uc77c \\ub610\\ub294 \\uccb4\\uacb0\\uc77c")
_BOND_CODE = u("\\ucc44\\uad8c \\ucee8\\ubca4\\uc158 \\ucf54\\ub4dc (\\uc608: bond_krw_ktb)")
_DISC_CURVE_PRICING = u("\\ud560\\uc778 \\uace1\\uc120 \\ub370\\uc774\\ud130 (NPV \\uacc4\\uc0b0\\uc6a9)")
_INDEX_CURVE = u("\\ubcc0\\ub3d9\\uae08\\ub9ac \\uc9c0\\ud45c \\uace1\\uc120 (\\uc608: CD \\uae08\\ub9ac)")
_SPREAD = u("\\ubcc0\\ub3d9\\uae08\\ub9ac \\uc2a4\\ud504\\ub808\\ub4dc (\\uc5f0\\uac04 \\ube44\\uc728)")
_TRADE_DATE = u("\\uac70\\ub798 \\uccb4\\uacb0\\uc77c")
_SWAP_CODE = u("\\uc2a4\\uc651 \\ucee8\\ubca4\\uc158 \\ucf54\\ub4dc (\\uc608: swap_krw_cd)")
_SWAP_SIDE = u("\\ub808\\uadf8 \\ubc29\\ud5a5. rec(\\uace0\\uc815 \\uc218\\ucde8)\\u00b7pay(\\uace0\\uc815 \\uc9c0\\uae09)")
_DEFAULT_CURVE = u("\\ubd80\\ub3c4\\ud655\\ub960 \\uace1\\uc120 (\\uc2e0\\uc6a9 \\ud3c9\\uac00\\uc6a9)")
_TENORS = u("\\ub9cc\\uae30 \\ubaa9\\ub85d (1M, 3Y \\ub4f1 \\ud14c\\ub108)")
_VALUES = u("\\uac01 \\ub9cc\\uae30\\uc5d0 \\ub300\\uc751\\ud558\\ub294 \\uae08\\ub9ac \\uac12")
_INPUT_TYPE = u("\\uc785\\ub825 \\uae08\\ub9ac \\uc720\\ud615. spot\\u00b7forward\\u00b7discount")
_COMPOUNDING = u("\\ubcf5\\ub9ac \\ubc29\\uc2dd (cont, annual \\ub4f1)")
_OUTPUT_COMPOUNDING = u("\\ucd9c\\ub825 \\uae08\\ub9ac\\uc758 \\ubcf5\\ub9ac \\ubc29\\uc2dd")


PARAM_DOCS: Dict[str, List[ParamDoc]] = {
    # --- Stage 1: curve bootstrap (YieldCurveXLFunctions.cs) ---
    "BootstrapBond": [
        ("refDate", _REF_DATE),
        ("yieldQuoteData", _BOND_QUOTE),
        ("curveType", _CURVE_TYPE),
    ],
    "BootstrapIRS": [
        ("refDate", _REF_DATE),
        ("swapQuoteData", _SWAP_QUOTE),
        ("curveType", _CURVE_TYPE + u(". \\ube44\\uc5b4 \\uc788\\uc73c\\uba74 zero_krw_cd \\uae30\\ubcf8\\uac12")),
    ],
    "BootstrapIRSDual": [
        ("refDate", _REF_DATE),
        ("swapQuoteData", _SWAP_QUOTE),
        ("curveType", u("\\ubd80\\ud2b8\\uc2a4\\ud2b8\\ub7a9 \\ub300\\uc0c1 \\uace1\\uc120 \\ucee8\\ubca4\\uc158 (\\ud544\\uc218). externalDiscount \\uc124\\uc815 \\ud544\\uc694")),
        ("discountCurveData", _DISCOUNT_CURVE),
    ],
    "BootstrapSmithWilsonFSS": [
        ("refDate", _REF_DATE),
        ("curveData", _SW_CURVE),
        ("ufr", _UFR),
        ("alpha", _ALPHA),
        ("cpnPerYear", u("YTM(quote) \\uc785\\ub825 \\uc2dc \\uc5f0\\uac04 \\ucfe0\\ud3f0 \\uc9c0\\uae09 \\ud69f\\uc218")),
        ("outTimes", _OUT_TIMES),
    ],
    "SmithWilsonFitAlpha": [
        ("refDate", _REF_DATE),
        ("curveData", _SPOT_CURVE),
        ("ufr", _UFR),
        ("convergenceT", u("\\uc218\\ub839 \\ud310\\uc815 \\ub9cc\\uae30 (\\ub144 \\ub2e8\\uc704)")),
        ("tolerance", u("\\u03b1 \\ucd94\\uc815 \\ud5c8\\uc6a9 \\uc624\\ucc28")),
    ],
    "BootstrapCCBS": [
        ("refDate", _REF_DATE),
        ("basisQuoteData", _BASIS_QUOTE),
        ("curveType", u("CCBS \\uace1\\uc120 \\ucee8\\ubca4\\uc158 \\ucf54\\ub4dc. base/quote \\ud1b5\\ud654 \\uc778\\ub371\\uc2a4 \\uace1\\uc120 \\uc815\\uc758 \\ud3ec\\ud568")),
        ("baseCurveData", _BASE_CURVE),
        ("quoteCurveData", u("\\uc0c1\\ub300\\ud1b5\\ud654 \\uc778\\ub371\\uc2a4 \\uace1\\uc120 \\ub370\\uc774\\ud130")),
        ("fxSpot", u("\\uae30\\uc900\\ud1b5\\ud654 \\ub300 \\uc0c1\\ub300\\ud1b5\\ud654 \\ud658\\uc728 (\\uc2a4\\ud31f)")),
    ],
    "BootstrapCCFS": [
        ("refDate", _REF_DATE),
        ("fixedQuoteData", _CCFS_QUOTE),
        ("curveType", u("CCFS \\uace1\\uc120 \\ucee8\\ubca4\\uc158 \\ucf54\\ub4dc")),
        ("baseCurveData", _BASE_CURVE),
        ("fxRate", u("\\uae30\\uc900\\ud1b5\\ud654 \\ub300 \\uc678\\ud654 \\ud658\\uc728")),
    ],
    # --- Stage 2: curve transform / interpolate (YieldCurveXLFunctions.cs) ---
    "InterpolateYieldCurve": [
        ("refDate", _REF_DATE),
        ("curveData", _CURVE_DATA_ZD + u(". zero \\ub610\\ub294 discount \\uace1\\uc120\\ub9cc \\uc9c0\\uc6d0")),
        ("dateOrTime", _DATE_OR_TIME),
    ],
    "ShockYieldCurve": [
        ("refDate", _REF_DATE),
        ("curveData", _CURVE_DATA_ZD),
        ("shockCode", u("\\uc2dc\\ub098\\ub9ac\\uc624 \\ucf54\\ub4dc (\\uc608: shock_zero1bp). \\uae08\\ub9ac \\ucda9\\uaca9 \\uc720\\ud615 \\uc815\\uc758")),
        ("dateOrTime", _DATE_OR_TIME + u(". \\ube44\\uc5b4 \\uc788\\uc73c\\uba74 \\uace1\\uc120 \\uc804\\uccb4 \\uad6c\\uac04")),
        ("shockMultiple", u("\\ucda9\\uaca9 \\ubc30\\uc218 (\\uc608: 1.0 = 1bp \\uae30\\uc900)")),
        ("outputType", _OUTPUT_TYPE),
    ],
    "YieldCurve": [
        ("refDate", _REF_DATE),
        ("curveData", _CURVE_DATA_ZD),
        ("curveType", _CURVE_TYPE + u(". \\ube44\\uc5b4 \\uc788\\uc73c\\uba74 curveData\\uc758 \\ucf54\\ub4dc \\uc0ac\\uc6a9")),
    ],
    "ForwardRateFromYC": [
        ("curveData", _CURVE_DATA_ZD + u(". refDate\\uac00 \\ud3ec\\ud568\\ub41c \\uace1\\uc120 \\ud544\\uc694")),
        ("forwardStartDates", u("\\uc804\\ubc29 \\uae08\\ub9ac \\uc2dc\\uc791\\uc77c \\ubaa9\\ub85d")),
        ("forwardEndDates", u("\\uc804\\ubc29 \\uae08\\ub9ac \\uc885\\ub8cc\\uc77c \\ubaa9\\ub85d (\\uc2dc\\uc791\\uc77c\\uacfc \\ub3d9\\uc77c \\uae38\\uc774)")),
        ("compounding", _COMPOUNDING + u(". \\uae30\\ubcf8 cont")),
        ("frequency", u("\\ubcf5\\ub9ac \\uc8fc\\uae30 (annual \\ub4f1). compounding\\uc774 compounded\\uc77c \\ub54c \\uc0ac\\uc6a9")),
    ],
    "ConvertToCurve": [
        ("tenors", _TENORS),
        ("values", _VALUES),
        ("inputType", _INPUT_TYPE),
        ("compounding", _COMPOUNDING),
        ("output_compounding", _OUTPUT_COMPOUNDING + u(". \\uc5ec\\ub7ec \\ucef4\\ud30c\\uc6b4\\ub529 \\uacb0\\uacfc \\uceec\\ub7fc \\ucd9c\\ub825")),
    ],
    "ConvertToSpotRate": [
        ("tenors", _TENORS),
        ("values", _VALUES),
        ("inputType", _INPUT_TYPE),
        ("compounding", _COMPOUNDING),
        ("output_compounding", _OUTPUT_COMPOUNDING),
    ],
    "ConvertToForwardRate": [
        ("tenors", _TENORS),
        ("values", _VALUES),
        ("inputType", _INPUT_TYPE),
        ("compounding", _COMPOUNDING),
        ("output_compounding", _OUTPUT_COMPOUNDING),
    ],
    "ConvertToDiscount": [
        ("tenors", _TENORS),
        ("values", _VALUES),
        ("inputType", _INPUT_TYPE),
        ("compounding", _COMPOUNDING),
        ("output_compounding", _OUTPUT_COMPOUNDING),
    ],
    # --- Stage 3: date / rate utilities (YieldCurveXLFunctions.cs) ---
    "TenorToTimes": [
        ("tenors", u("\\ub9cc\\uae30 \\ud14c\\ub108 \\ubaa9\\ub85d (1M, 3Y \\ub4f1)\\uc744 \\uc5f0 \\ub2e8\\uc704 \\uacbd\\uacfc \\uc2dc\\uac04\\uc73c\\ub85c \\ubcc0\\ud658")),
    ],
    "DateToTimes": [
        ("dates", u("\\ubcc0\\ud658\\ud560 \\ub0a0\\uc9dc \\ubaa9\\ub85d")),
        ("refDate", u("\\uae30\\uc900\\uc77c. \\ube44\\uc5b4 \\uc788\\uc73c\\uba74 \\uc624\\ub298 \\ub0a0\\uc9dc")),
        ("daycounter", u("\\uc77c\\uc218\\uacc4\\uc0b0 \\uae30\\uc900 (\\uc608: Act365). \\uae30\\ubcf8 Act365")),
    ],
    "TimeToTenors": [
        ("times", u("\\uc5f0 \\ub2e8\\uc704 \\uacbd\\uacfc \\uc2dc\\uac04 \\ubc30\\uc5f4\\uc744 \\ud45c\\uc900 \\ub9cc\\uae30 \\ud14c\\ub108\\ub85c \\ubcc0\\ud658")),
    ],
    "AddTenorToDate": [
        ("dates", u("\\uae30\\uc900 \\ub0a0\\uc9dc \\ubaa9\\ub85d")),
        ("tenors", u("\\ub354\\ud560 \\ub9cc\\uae30 \\ud14c\\ub108 \\ubaa9\\ub85d (3M, 1Y \\ub4f1)")),
        ("calendar", u("\\uc601\\uc5c5\\uc77c \\uce98\\ub9b0\\ub354 (\\uc608: KR, Null). \\ube44\\uc5b4 \\uc788\\uc73c\\uba74 NullCalendar")),
        ("lagDays", u("\\uacb0\\uc81c\\uc77c \\ub9c0\\uc5f0 \\uc77c\\uc218 (T+lag)")),
    ],
    "ToCompoundRate": [
        ("dateOrTimes", u("\\uae08\\ub9ac \\ubcc0\\ud658 \\uae30\\uc900 \\uc77c\\uc790 \\ub610\\ub294 time")),
        ("contiRate", u("\\uc785\\ub825 \\uc5f0\\uc18d\\ubcf5\\ub9ac \\uae08\\ub9ac \\ubc30\\uc5f4")),
        ("freqPerYear", u("\\ubaa9\\ud45c \\ubcf5\\ub9ac \\uc8fc\\uae30 (\\uc5f0 \\uac04 \\ud69f\\uc218)")),
        ("dayCounter", u("\\uc77c\\uc218\\uacc4\\uc0b0 \\uae30\\uc900")),
        ("calendar", u("\\uc601\\uc5c5\\uc77c \\uce98\\ub9b0\\ub354")),
        ("refDate", u("\\uae30\\uc900\\uc77c (dayCounter \\uacc4\\uc0b0\\uc6a9)")),
    ],
    "ToContinuousRate": [
        ("dateOrTimes", u("\\uae08\\ub9ac \\ubcc0\\ud658 \\uae30\\uc900 \\uc77c\\uc790 \\ub610\\ub294 time")),
        ("compoundRate", u("\\uc785\\ub825 \\ubcf5\\ub9ac \\uae08\\ub9ac \\ubc30\\uc5f4")),
        ("freqPerYear", u("\\uc785\\ub825 \\uae08\\ub9ac\\uc758 \\ubcf5\\ub9ac \\uc8fc\\uae30 (\\uc5f0 \\uac04 \\ud69f\\uc218)")),
        ("dayCounter", u("\\uc77c\\uc218\\uacc4\\uc0b0 \\uae30\\uc900")),
        ("calendar", u("\\uc601\\uc5c5\\uc77c \\uce98\\ub9b0\\ub354")),
        ("refDate", u("\\uae30\\uc900\\uc77c")),
    ],
    # --- Stage 4: bonds / loans ---
    "FixedBond": [
        ("notional", _NOTIONAL),
        ("maturity", _MATURITY),
        ("fixedRate", _FIXED_RATE),
        ("issueDate", _ISSUE_DATE),
        ("bondCode", _BOND_CODE),
        ("curveData", _DISC_CURVE_PRICING),
        ("valueDate", _VALUE_DATE),
        ("outputType", _OUTPUT_TYPE),
    ],
    "FloatBond": [
        ("notional", _NOTIONAL),
        ("maturity", _MATURITY),
        ("spread", _SPREAD),
        ("issueDate", _ISSUE_DATE),
        ("bondCode", _BOND_CODE),
        ("indexCurveData", _INDEX_CURVE),
        ("curveData", _DISC_CURVE_PRICING),
        ("valueDate", _VALUE_DATE),
        ("outputType", _OUTPUT_TYPE),
    ],
    "BondForward": [
        ("notional", _NOTIONAL),
        ("delivery", u("\\uc120\\ub3c4(\\uc778\\ub3c4) \\uc77c. \\ub0a0\\uc9dc \\ub610\\ub294 \\ud14c\\ub108")),
        ("strike", u("\\uc120\\ub3c4 \\uac00\\uaca9 (\\ucc44\\uad8c \\uac00\\uaca9 \\uae30\\uc900)")),
        ("maturity", u("\\uae30\\uc900 \\ucc44\\uad8c \\ub9cc\\uae30")),
        ("fixedRate", _FIXED_RATE),
        ("bondSide", u("\\ucc44\\uad8c \\ud3ec\\uc9c0\\uc785\\uc7a5. buy\\u00b7sell")),
        ("issueDate", _ISSUE_DATE),
        ("bondCode", _BOND_CODE),
        ("curveData", _DISC_CURVE_PRICING),
        ("valueDate", _VALUE_DATE),
        ("outputType", _OUTPUT_TYPE),
    ],
    "IsinBond": [
        ("isin", u("ISIN \\ucf54\\ub4dc (12\\uc790\\ub9ac)")),
        ("notional", _NOTIONAL),
        ("curveData", _DISC_CURVE_PRICING),
        ("valueDate", _VALUE_DATE),
        ("outputType", _OUTPUT_TYPE),
    ],
    "IsinBondInfo": [
        ("isin", u("ISIN \\ucf54\\ub4dc. \\ucc44\\uad8c \\uae30\\ubcf8 \\uc815\\ubcf4(\\ub9cc\\uae30\\u00b7\\ucfe0\\ud3f0\\u00b7\\ubc1c\\ud589\\uc77c \\ub4f1) \\uc870\\ud68c")),
    ],
    "FixedLoan": [
        ("principal", u("\\ub300\\ucd9c \\uc6d0\\uae08")),
        ("balance", u("\\ud604\\uc7ac \\uc794\\uc561 (\\uc0c1\\ud658 \\uacc4\\uc0b0 \\uae30\\uc900)")),
        ("maturity", _MATURITY),
        ("fixedRate", _FIXED_RATE),
        ("loanSide", u("\\ub300\\ucd9c \\ubc29\\ud5a5. buy(long)\\u00b7sell(short)")),
        ("loanDate", u("\\ub300\\ucd9c \\uc2e4\\ud589\\uc77c")),
        ("loanCode", u("\\ub300\\ucd9c \\ucee8\\ubca4\\uc158 \\ucf54\\ub4dc (\\uc608: loan_krw_fixed)")),
        ("gracePeriod", u("\\uc6d0\\ub9ac\\uae08 \\uc0c1\\ud658 \\uac70\\uce58 \\uae30\\uac04 (\\uc6d4 \\ub610\\ub294 \\ud68c\\ucc28)")),
        ("curveData", _DISC_CURVE_PRICING),
        ("defaultData", _DEFAULT_CURVE + u(". \\uc120\\ud0dd")),
        ("earlyRedemRate", u("\\uc911\\ub3c4\\uc0c1\\ud658 \\uc218\\uc218\\ub8cc\\uc728")),
        ("valueDate", _VALUE_DATE),
        ("outputType", _OUTPUT_TYPE),
    ],
    "FloatLoan": [
        ("principal", u("\\ub300\\ucd9c \\uc6d0\\uae08")),
        ("balance", u("\\ud604\\uc7ac \\uc794\\uc561")),
        ("maturity", _MATURITY),
        ("spread", _SPREAD),
        ("loanSide", u("\\ub300\\ucd9c \\ubc29\\ud5a5. long\\u00b7short")),
        ("gracePeriod", u("\\uc6d0\\ub9ac\\uae08 \\uc0c1\\ud658 \\uac70\\uce58 \\uae30\\uac04")),
        ("amortization", u("\\uc0c1\\ud658 \\ubc29\\uc2dd (bullet \\ub4f1)")),
        ("inArrears", u("\\uc774\\uc790 \\uc9c0\\uae09 \\uc2dc\\uc810. false=\\uc120\\uc9c0\\uae09, true=\\ud6c4\\uc9c0\\uae09")),
        ("loanDate", u("\\ub300\\ucd9c \\uc2e4\\ud589\\uc77c")),
        ("loanCode", u("\\ub300\\ucd9c \\ucee8\\ubca4\\uc158 \\ucf54\\ub4dc (\\uc608: loan_krw_float)")),
        ("indexCurveData", _INDEX_CURVE),
        ("curveData", _DISC_CURVE_PRICING),
        ("defaultData", _DEFAULT_CURVE + u(". \\uc120\\ud0dd")),
        ("earlyRedemRate", u("\\uc911\\ub3c4\\uc0c1\\ud658 \\uc218\\uc218\\ub8cc\\uc728")),
        ("valueDate", _VALUE_DATE),
        ("outputType", _OUTPUT_TYPE),
    ],
    # --- Stage 5: swaps / TRS ---
    "VanillaSwap": [
        ("notional", _NOTIONAL),
        ("maturityTenor", _MATURITY_TENOR),
        ("fixedRate", _FIXED_RATE),
        ("swapSide", _SWAP_SIDE),
        ("tradeDate", _TRADE_DATE),
        ("swapCode", _SWAP_CODE),
        ("curveData", _DISC_CURVE_PRICING),
        ("valueDate", _VALUE_DATE),
        ("outputType", _OUTPUT_TYPE),
    ],
    "VanillaCRSwap": [
        ("notional", _NOTIONAL),
        ("maturityTenor", _MATURITY_TENOR),
        ("fixedRate", _FIXED_RATE),
        ("swapSide", _SWAP_SIDE),
        ("exchangeRate", u("\\uace0\\uc815 \\ud658\\uc728 (\\ucd08\\uae30 \\uad50\\ud658 \\uac00\\uaca9)")),
        ("tradeDate", _TRADE_DATE),
        ("swapCode", u("CRS \\ucee8\\ubca4\\uc158 \\ucf54\\ub4dc (\\uc608: ccs_usdkrw_sofr_fixed)")),
        ("baseCurveData", _BASE_CURVE),
        ("quoteCurveData", u("\\uc0c1\\ub300\\ud1b5\\ud654 \\ud560\\uc778 \\uace1\\uc120")),
        ("fxSpot", u("\\ud604\\uc7ac \\ud658\\uc728 (\\uc2a4\\ud31f)")),
        ("valueDate", _VALUE_DATE),
        ("outputType", _OUTPUT_TYPE),
    ],
    "VanillaBSwap": [
        ("notional", _NOTIONAL),
        ("maturityTenor", _MATURITY_TENOR),
        ("basisSpread", u("\\ud1b5\\ud654\\ubcc4 \\ubcc0\\ub3d9 \\uc9c0\\ud45c \\uac04 \\ubca0\\uc774\\uc2dc\\uc2a4 \\uc2a4\\ud504\\ub808\\ub4dc")),
        ("swapSide", _SWAP_SIDE),
        ("exchangeRate", u("\\uace0\\uc815 \\ud658\\uc728")),
        ("tradeDate", _TRADE_DATE),
        ("swapCode", u("CCBS \\ucee8\\ubca4\\uc158 \\ucf54\\ub4dc (\\uc608: ccbs_usdkrw_sofr_cd)")),
        ("baseCurveData", _BASE_CURVE),
        ("quoteCurveData", u("\\uc0c1\\ub300\\ud1b5\\ud654 \\uc778\\ub371\\uc2a4 \\uace1\\uc120")),
        ("fxSpot", u("\\ud658\\uc728 (\\uc2a4\\ud31f)")),
        ("valueDate", _VALUE_DATE),
        ("outputType", _OUTPUT_TYPE),
    ],
    "GeneralSwap": [
        ("inputData", u("\\uc77c\\ubc18 \\uc2a4\\uc651 \\uc785\\ub825 \\ud14c\\uc774\\ube14 (name\\u00b7value). \\uac70\\ub798 \\uc815\\ubcf4\\uc640 leg1/leg2 \\uc870\\uac74\\uc744 \\uc815\\uc758")),
    ],
    "TRSFixed": [
        ("refAssetType", u("\\uae30\\uc900 \\uc790\\uc0b0 \\uc720\\ud615 (\\uc608: FixedBond)")),
        ("refAssetData", u("\\uae30\\uc900 \\uc790\\uc0b0 \\ud30c\\ub77c\\ubbf8\\ud130 (\\ucc44\\uad8c \\uc870\\uac74 \\ub4f1)")),
        ("notional", _NOTIONAL),
        ("maturityTenor", _MATURITY_TENOR),
        ("fixedRate", u("TRS \\uace0\\uc815 \\ud504\\ub9c0 \\uae08\\ub9ac")),
        ("tradeDate", _TRADE_DATE),
        ("swapCode", u("TRS \\ucee8\\ubca4\\uc158 \\ucf54\\ub4dc (\\uc608: trs_krw_fixedbond)")),
        ("curveData", _DISC_CURVE_PRICING),
        ("valueDate", _VALUE_DATE),
        ("outputType", _OUTPUT_TYPE),
    ],
    # --- Stage 6: credit / options ---
    "CDS": [
        ("notional", _NOTIONAL),
        ("maturityTenor", _MATURITY_TENOR),
        ("fixedRate", u("CDS \\uace0\\uc815 \\uc2a4\\ud504\\ub808\\ub4dc (\\ucfe0\\ud3f0 \\uae08\\ub9ac)")),
        ("tradeDate", _TRADE_DATE),
        ("swapCode", u("CDS \\ucee8\\ubca4\\uc158 \\ucf54\\ub4dc (\\uc608: cds_krw)")),
        ("defaultCurveData", _DEFAULT_CURVE),
        ("curveData", _DISC_CURVE_PRICING),
        ("valueDate", _VALUE_DATE),
        ("outputType", _OUTPUT_TYPE),
    ],
    "CLNFixed": [
        ("notional", _NOTIONAL),
        ("maturityTenor", _MATURITY_TENOR),
        ("fixedRate", _FIXED_RATE),
        ("issueDate", _ISSUE_DATE),
        ("bondCode", _BOND_CODE),
        ("defaultCurveData", _DEFAULT_CURVE),
        ("curveData", _DISC_CURVE_PRICING),
        ("valueDate", _VALUE_DATE),
        ("outputType", _OUTPUT_TYPE),
    ],
    "CLNFloat": [
        ("notional", _NOTIONAL),
        ("maturityTenor", _MATURITY_TENOR),
        ("spread", _SPREAD),
        ("issueDate", _ISSUE_DATE),
        ("bondCode", _BOND_CODE),
        ("defaultCurveData", _DEFAULT_CURVE),
        ("indexCurveData", _INDEX_CURVE),
        ("curveData", _DISC_CURVE_PRICING),
        ("valueDate", _VALUE_DATE),
        ("outputType", _OUTPUT_TYPE),
    ],
    "Swaption": [
        ("notional", _NOTIONAL),
        ("optionTenor", u("\\uc635\\uc158 \\ub9cc\\uae30 \\ud14c\\ub108 (\\uc608: 1Y)")),
        ("swapTenor", u("\\uae30\\uc900 \\uc2a4\\uc651 \\ub9cc\\uae30 (\\uc608: 5Y)")),
        ("strike", u("\\ud589\\uc0ac\\uac00\\uae30 \\uae08\\ub9ac. \\uc22b\\uc790 \\ub610\\ub294 atm")),
        ("swapSide", _SWAP_SIDE),
        ("tradeDate", _TRADE_DATE),
        ("swaptionCode", u("\\uc2a4\\uc651\\uc158 \\ucee8\\ubca4\\uc158 \\ucf54\\ub4dc (\\uc608: swaption_krw_cd)")),
        ("normalVol", u("\\ub178\\uba38 \\ubcfc\\ub77c\\ud2f8\\ub9ac\\ud2f0 (\\uc5f0\\uac04 \\ube44\\uc728)")),
        ("curveData", _DISC_CURVE_PRICING),
        ("valueDate", _VALUE_DATE),
        ("outputType", _OUTPUT_TYPE),
    ],
}


def get_param_docs(func_name: str, args: str) -> List[ParamDoc]:
    inner = args[1:-1] if args.startswith("(") and args.endswith(")") else args
    param_names = [p.strip() for p in inner.split(",") if p.strip()]
    docs = PARAM_DOCS.get(func_name, [])
    doc_map = dict(docs)
    result: List[ParamDoc] = []
    for name in param_names:
        result.append((name, doc_map.get(name, "")))
    return result
