# ASCII-only generator: function detail pages + pricing-api catalog (UTF-8 safe)
from __future__ import annotations

import html
import json
import pathlib
import shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
TARGET = ROOT / "pricing-api.html"
FUNC_DIR = ROOT / "functions"
SAMPLES_DIR = FUNC_DIR / "samples"
MARKER = '        <div class="section-header">\n          <span class="section-label">Documentation</span>'
TEST_JSON_DIR = ROOT.parent / "TestPricing" / "API" / "json"
LOCAL_JSON_DIR = ROOT / "api" / "json"

JSON_ALIASES = {
    "BootstrapBond": "BootstrapBond1.json",
}


def u(s: str) -> str:
    return s.encode("ascii").decode("unicode_escape")


def sig_html(name: str, args: str, indent: str = "") -> str:
    inner = args[1:-1] if args.startswith("(") and args.endswith(")") else args
    return (
        indent
        + '<code class="func-sig"><span class="func-fn">'
        + name
        + '</span><span class="func-paren">(</span><span class="func-params">'
        + inner
        + '</span><span class="func-paren">)</span></code>'
    )


def item(name: str, args: str, desc: str) -> str:
    return (
        "              <li>\n"
        + sig_html(name, args, "                ")
        + "\n"
        '                <div class="func-desc-row">\n'
        '                  <p class="func-desc">'
        + desc
        + "</p>\n"
        '                  <a class="card-version func-detail-link" href="functions/'
        + name
        + '.html">'
        + u("\\uc0c1\\uc138")
        + "</a>\n"
        "                </div>\n"
        "              </li>\n"
    )


def category(title: str, count: int, entries: list[tuple[str, str, str]]) -> str:
    body = "".join(item(n, a, d) for n, a, d in entries)
    return (
        '          <details class="func-category">\n'
        '            <summary class="func-category-summary">\n'
        '              <span class="func-category-title">'
        + title
        + '</span>\n              <span class="func-category-meta">'
        + str(count)
        + u("\\uac1c")
        + "</span>\n"
        "            </summary>\n"
        '            <ul class="func-list">\n'
        + body
        + "            </ul>\n"
        "          </details>\n"
    )


DATA: list[tuple[str, int, list[tuple[str, str, str]]]] = [
    (
        u("\\uace1\\uc120 \\ubd80\\ud2b8\\uc2a4\\ud2b8\\ub7a9"),
        7,
        [
            ("BootstrapBond", "(refDate, yieldQuoteData, curveType)", u("\\ucc44\\uad8c Par\\u00b7YTM \\uacac\\uc801\\uc73c\\ub85c \\ud560\\uc778\\u00b7\\uc2a4\\ud31f \\uae08\\ub9ac \\uace1\\uc120\\uc744 \\uad6c\\ucd95\\ud569\\ub2c8\\ub2e4.")),
            ("BootstrapIRS", "(refDate, swapQuoteData, curveType)", u("\\uae08\\ub9ac\\uc2a4\\uc651 \\uacac\\uc801\\uc73c\\ub85c IBOR/OIS \\ud560\\uc778\\u00b7\\uc804\\ubc29 \\uace1\\uc120\\uc744 \\ubd80\\ud2b8\\uc2a4\\ud2b8\\ub7a9\\ud569\\ub2c8\\ub2e4.")),
            ("BootstrapIRSDual", "(refDate, swapQuoteData, curveType, discountCurveData)", u("\\uc2a4\\uc651 \\uace1\\uc120\\uacfc \\ubcc4\\ub3c4 \\ud560\\uc778 \\uace1\\uc120\\uc744 \\uc0ac\\uc6a9\\ud558\\ub294 \\ub4c0\\uc5bc \\ucee4\\ube0c \\ubd80\\ud2b8\\uc2a4\\ud2b8\\ub7a9\\uc744 \\uc218\\ud589\\ud569\\ub2c8\\ub2e4.")),
            ("BootstrapSmithWilsonFSS", "(refDate, curveData, ufr, alpha, cpnPerYear, outTimes)", u("Smith-Wilson \\ubc29\\ubc95\\uc73c\\ub85c \\uc7a5\\uae30 \\uae08\\ub9ac \\uace1\\uc120\\uc744 \\uc0dd\\uc131\\ud569\\ub2c8\\ub2e4.")),
            ("SmithWilsonFitAlpha", "(refDate, curveData, ufr, convergenceT, tolerance)", u("Smith-Wilson \\ubcf4\\uac04\\uc5d0 \\uc0ac\\uc6a9\\ud560 \\uc218\\ub839 \\ud30c\\ub77c\\ubbf8\\ud130 \\u03b1\\ub97c \\uc2dc\\uc7a5 \\ub370\\uc774\\ud130\\uc5d0 \\ub9de\\uac8c \\ucd94\\uc815\\ud569\\ub2c8\\ub2e4.")),
            ("BootstrapCCBS", "(refDate, basisQuoteData, curveType, baseCurveData, quoteCurveData, fxSpot)", u("\\uad50\\ucc28\\ud1b5\\ud654 \\ubca0\\uc774\\uc2dc\\uc2a4 \\uc2a4\\uc651 \\uacac\\uc801\\uc73c\\ub85c CCBS \\uace1\\uc120\\uc744 \\uad6c\\ucd95\\ud569\\ub2c8\\ub2e4.")),
            ("BootstrapCCFS", "(refDate, fixedQuoteData, curveType, baseCurveData, fxRate)", u("\\uad50\\ucc28\\ud1b5\\ud654 \\uace0\\uc815\\uae08\\ub9ac \\uc2a4\\uc651 \\uacac\\uc801\\uc73c\\ub85c \\uc678\\ud654 \\ud560\\uc778 \\uace1\\uc120\\uc744 \\ubd80\\ud2b8\\uc2a4\\ud2b8\\ub7a9\\ud569\\ub2c8\\ub2e4.")),
        ],
    ),
    (
        u("\\uace1\\uc120 \\ubcc0\\ud658\\u00b7\\ubcf4\\uac04"),
        8,
        [
            ("InterpolateYieldCurve", "(refDate, curveData, dateOrTime)", u("\\uad6c\\ucd95\\ub41c \\uace1\\uc120\\uc5d0\\uc11c \\ud2b9\\uc815 \\uc77c\\uc790\\u00b7\\ub9cc\\uae30 \\uc9c0\\uc810\\uc758 \\uae08\\ub9ac\\ub97c \\ubcf4\\uac04\\ud569\\ub2c8\\ub2e4.")),
            ("ShockYieldCurve", "(refDate, curveData, shockCode, dateOrTime, shockMultiple, outputType)", u("\\ubcd1\\ub82c\\u00b7\\uc2a4\\ud3ec\\ud2b8 \\ub4f1 \\uc2dc\\ub098\\ub9ac\\uc624 \\ucda9\\uaca9\\uc744 \\uc801\\uc6a9\\ud55c \\ucda9\\uaca9 \\uace1\\uc120\\uc744 \\uc0b0\\ucd9c\\ud569\\ub2c8\\ub2e4.")),
            ("YieldCurve", "(refDate, curveData, curveType)", u("\\uace1\\uc120 \\ub370\\uc774\\ud130\\ub85c YieldCurve \\uac1d\\uccb4\\ub97c \\uc0dd\\uc131\\ud558\\uace0 \\uc870\\ud68c\\ud569\\ub2c8\\ub2e4.")),
            ("ForwardRateFromYC", "(curveData, forwardStartDates, forwardEndDates, compounding, frequency)", u("yield curve\\ub85c\\ubd80\\ud130 \\uc9c0\\uc815 \\uad6c\\uac04\\uc758 \\uc804\\ubc29 \\uae08\\ub9ac\\ub97c \\uacc4\\uc0b0\\ud569\\ub2c8\\ub2e4.")),
            ("ConvertToCurve", "(tenors, values, inputType, compounding, output_compounding)", u("\\ud14c\\ub108\\u00b7\\uae08\\ub9ac \\uc2dc\\ub9ac\\uc988\\ub97c \\ub2e4\\ub978 \\ucef4\\ud30c\\uc6b4\\ub529 \\ubc29\\uc2dd\\uc758 \\uace1\\uc120 \\ud615\\ud0dc\\ub85c \\ubcc0\\ud658\\ud569\\ub2c8\\ub2e4.")),
            ("ConvertToSpotRate", "(tenors, values, inputType, compounding, output_compounding)", u("Par\\u00b7Forward\\u00b7Discount \\ub4f1 \\uc785\\ub825 \\uae08\\ub9ac\\ub97c \\uc2a4\\ud31f \\uae08\\ub9ac\\ub85c \\ubcc0\\ud658\\ud569\\ub2c8\\ub2e4.")),
            ("ConvertToForwardRate", "(tenors, values, inputType, compounding, output_compounding)", u("\\uc785\\ub825 \\uae08\\ub9ac\\ub97c \\uc804\\ubc29 \\uae08\\ub9ac\\ub85c \\ubcc0\\ud658\\ud569\\ub2c8\\ub2e4.")),
            ("ConvertToDiscount", "(tenors, values, inputType, compounding, output_compounding)", u("\\uc785\\ub825 \\uae08\\ub9ac\\ub97c \\ud560\\uc778\\uacc4\\uc218\\ub85c \\ubcc0\\ud658\\ud569\\ub2c8\\ub2e4.")),
        ],
    ),
    (
        u("\\uc77c\\uc790\\u00b7\\uae08\\ub9ac \\uc720\\ud2f8\\ub9ac\\ud2f0"),
        6,
        [
            ("TenorToTimes", "(tenors)", u("\\ub9cc\\uae30 \\ud45c\\uae30(1M, 3Y \\ub4f1)\\ub97c \\uc5f0 \\ub2e8\\uc704 \\uacbd\\uacfc \\uc2dc\\uac04\\uc73c\\ub85c \\ubcc0\\ud658\\ud569\\ub2c8\\ub2e4.")),
            ("DateToTimes", "(dates, refDate, daycounter)", u("\\ub0a0\\uc9dc\\ub97c \\uae30\\uc900\\uc77c \\ub300\\ube44 \\uc5f0 \\ub2e8\\uc704 \\uacbd\\uacfc \\uc2dc\\uac04\\uc73c\\ub85c \\ubcc0\\ud658\\ud569\\ub2c8\\ub2e4.")),
            ("TimeToTenors", "(times)", u("\\uc5f0 \\ub2e8\\uc704 \\uc2dc\\uac04\\uc744 \\ud45c\\uc900 \\ub9cc\\uae30 \\ud14c\\ub108\\ub85c \\uc5ed\\ubcc0\\ud658\\ud569\\ub2c8\\ub2e4.")),
            ("AddTenorToDate", "(dates, tenors, calendar, lagDays)", u("\\ub0a0\\uc9dc\\uc5d0 \\ub9cc\\uae30 \\ud14c\\ub108\\ub97c \\ub354\\ud574 \\uc0c8 \\ub9cc\\uae30\\uc77c\\uc744 \\uacc4\\uc0b0\\ud569\\ub2c8\\ub2e4.")),
            ("ToCompoundRate", "(dateOrTimes, contiRate, freqPerYear, dayCounter, calendar, refDate)", u("\\uc5f0\\uc18d\\ubcf5\\ub9ac \\uae08\\ub9ac\\ub97c \\uc9c0\\uc815 \\ubcf5\\ub9ac \\uc8fc\\uae30\\uc758 \\ubcf5\\ub9ac \\uae08\\ub9ac\\ub85c \\ubcc0\\ud658\\ud569\\ub2c8\\ub2e4.")),
            ("ToContinuousRate", "(dateOrTimes, compoundRate, freqPerYear, dayCounter, calendar, refDate)", u("\\ubcf5\\ub9ac \\uae08\\ub9ac\\ub97c \\uc5f0\\uc18d\\ubcf5\\ub9ac \\uae08\\ub9ac\\ub85c \\ubcc0\\ud658\\ud569\\ub2c8\\ub2e4.")),
        ],
    ),
    (
        u("\\ucc44\\uad8c\\u00b7\\ub300\\ucd9c"),
        7,
        [
            ("FixedBond", "(notional, maturity, fixedRate, issueDate, bondCode, curveData, valueDate, outputType)", u("\\uace0\\uc815\\uae08\\ub9ac\\ucc44\\uad8c\\uc758 \\uac00\\uaca9, \\ud604\\uae08\\ud750\\ub984, DV01\\u00b7\\ub4c0\\ub808\\uc774\\uc158\\uc744 \\uc0b0\\ucd9c\\ud569\\ub2c8\\ub2e4.")),
            ("FloatBond", "(notional, maturity, spread, issueDate, bondCode, indexCurveData, curveData, valueDate, outputType)", u("\\ubcc0\\ub3d9\\uae08\\ub9ac\\ucc44\\uad8c\\uc758 NPV\\u00b7\\ucfe0\\ud3f0\\u00b7\\ubbfc\\uac10\\ub3c4\\ub97c \\ud3c9\\uac00\\ud569\\ub2c8\\ub2e4.")),
            ("BondForward", "(notional, delivery, strike, maturity, fixedRate, bondSide, issueDate, bondCode, curveData, valueDate, outputType)", u("\\ucc44\\uad8c \\uc120\\ub3c4 \\uacc4\\uc57d\\uc758 \\uacf5\\uc815\\uac00\\uce58\\ub97c \\uacc4\\uc0b0\\ud569\\ub2c8\\ub2e4.")),
            ("IsinBond", "(isin, notional, curveData, valueDate, outputType)", u("ISIN \\ucf54\\ub4dc \\uae30\\ubc18 \\ucc44\\uad8c \\ud3c9\\uac00\\ub97c \\uc218\\ud589\\ud569\\ub2c8\\ub2e4.")),
            ("IsinBondInfo", "(isin)", u("ISIN\\uc5d0 \\ud574\\ub2f9\\ud558\\ub294 \\ucc44\\uad8c \\uae30\\ubcf8 \\uc815\\ubcf4\\ub97c \\uc870\\ud68c\\ud569\\ub2c8\\ub2e4.")),
            ("FixedLoan", "(principal, balance, maturity, fixedRate, loanSide, loanDate, loanCode, gracePeriod, curveData, defaultData, earlyRedemRate, valueDate, outputType)", u("\\uace0\\uc815\\uae08\\ub9ac \\ub300\\ucd9c\\uc758 NPV, \\uc0c1\\ud658 \\uc2a4\\ucf00\\uc904 \\ubc0f \\ubd80\\ub3c4 \\ubc18\\uc601 \\ud3c9\\uac00\\ub97c \\uc218\\ud589\\ud569\\ub2c8\\ub2e4.")),
            ("FloatLoan", "(principal, balance, maturity, spread, loanSide, gracePeriod, amortization, inArrears, loanDate, loanCode, indexCurveData, curveData, defaultData, earlyRedemRate, valueDate, outputType)", u("\\ubcc0\\ub3d9\\uae08\\ub9ac \\ub300\\ucd9c\\uc758 NPV\\u00b7OAS\\u00b7\\uc2a4\\ud504\\ub808\\ub4dc \\ub4f1\\uc744 \\ud3c9\\uac00\\ud569\\ub2c8\\ub2e4.")),
        ],
    ),
    (
        u("\\uc2a4\\uc651\\u00b7TRS"),
        5,
        [
            ("VanillaSwap", "(notional, maturityTenor, fixedRate, swapSide, tradeDate, swapCode, curveData, valueDate, outputType)", u("\\uc774\\uc790\\uc728 \\uc2a4\\uc651(\\uace0\\uc815 vs \\ubcc0\\ub3d9)\\uc758 NPV, \\ub808\\uadf8 PV, DV01\\uc744 \\uc0b0\\ucd9c\\ud569\\ub2c8\\ub2e4.")),
            ("VanillaCRSwap", "(notional, maturityTenor, fixedRate, swapSide, exchangeRate, tradeDate, swapCode, baseCurveData, quoteCurveData, fxSpot, valueDate, outputType)", u("\\uad50\\ucc28\\ud1b5\\ud654 \\uc2a4\\uc651(CRS)\\uc758 \\uc591 \\ud1b5\\ud654 \\ub808\\uadf8 NPV\\uc640 \\uc21c\\uc790\\uc0b0\\uac00\\uce58\\ub97c \\ud3c9\\uac00\\ud569\\ub2c8\\ub2e4.")),
            ("VanillaBSwap", "(notional, maturityTenor, basisSpread, swapSide, exchangeRate, tradeDate, swapCode, baseCurveData, quoteCurveData, fxSpot, valueDate, outputType)", u("\\ud1b5\\ud654\\ubcc4 \\ubcc0\\ub3d9\\uae08\\ub9ac \\uc9c0\\ud45c\\uac00 \\ub2e4\\ub978 \\ubca0\\uc774\\uc2dc\\uc2a4 \\uc2a4\\uc651\\uc744 \\ud3c9\\uac00\\ud569\\ub2c8\\ub2e4.")),
            ("GeneralSwap", "(inputData)", u("\\ucee4\\uc2a4\\ud140 \\uc2a4\\ucf00\\uc904\\u00b7\\ub808\\uadf8 \\uad6c\\uc870\\ub97c \\uac00\\uc9c4 \\uc77c\\ubc18 \\uc2a4\\uc651\\uc744 \\ud3c9\\uac00\\ud569\\ub2c8\\ub2e4. inputData \\ud14c\\uc774\\ube14\\uc5d0 \\ub808\\uadf8\\ubcc4 \\uc870\\uac74\\uc744 \\uc815\\uc758\\ud569\\ub2c8\\ub2e4.")),
            ("TRSFixed", "(refAssetType, refAssetData, notional, maturityTenor, fixedRate, tradeDate, swapCode, curveData, valueDate, outputType)", u("\\uace0\\uc815\\uae08\\ub9ac \\ucd1d\\uc218\\uc775\\uc2a4\\uc651(TRS)\\uc758 \\uacf5\\uc815\\uac00\\uce58\\ub97c \\uacc4\\uc0b0\\ud569\\ub2c8\\ub2e4.")),
        ],
    ),
    (
        u("\\uc2e0\\uc6a9\\u00b7\\uc635\\uc158"),
        4,
        [
            ("CDS", "(notional, maturityTenor, fixedRate, tradeDate, swapCode, defaultCurveData, curveData, valueDate, outputType)", u("\\uc2e0\\uc6a9\\ubd80\\ub3c4\\uc2a4\\uc651(CDS)\\uc758 NPV, \\uae30\\ubcf8\\uc2a4\\ud504\\ub808\\ub4dc, \\ub9ac\\uc2a4\\ud06c \\uc9c0\\ud45c\\ub97c \\ud3c9\\uac00\\ud569\\ub2c8\\ub2e4.")),
            ("CLNFixed", "(notional, maturityTenor, fixedRate, issueDate, bondCode, defaultCurveData, curveData, valueDate, outputType)", u("\\uace0\\uc815\\uae08\\ub9ac \\uc2e0\\uc6a9\\uc5f0\\uacc4\\ucc44\\uad8c(CLN)\\uc758 \\uac00\\uaca9\\uc744 \\uc0b0\\ucd9c\\ud569\\ub2c8\\ub2e4.")),
            ("CLNFloat", "(notional, maturityTenor, spread, issueDate, bondCode, defaultCurveData, indexCurveData, curveData, valueDate, outputType)", u("\\ubcc0\\ub3d9\\uae08\\ub9ac CLN\\uc758 NPV\\u00b7\\uc2a4\\ud504\\ub808\\ub4dc \\ub4f1\\uc744 \\ud3c9\\uac00\\ud569\\ub2c8\\ub2e4.")),
            ("Swaption", "(notional, optionTenor, swapTenor, strike, swapSide, tradeDate, swaptionCode, normalVol, curveData, valueDate, outputType)", u("\\uae08\\ub9ac\\uc2a4\\uc651\\uc158\\uc758 \\uac00\\uaca9\\uacfc Delta\\u00b7Vega \\ub4f1 \\ubbfc\\uac10\\ub3c4\\ub97c \\uc0b0\\ucd9c\\ud569\\ub2c8\\ub2e4.")),
        ],
    ),
]


def iter_functions() -> list[tuple[str, str, str, str]]:
    rows: list[tuple[str, str, str, str]] = []
    for cat_title, _count, entries in DATA:
        for name, args, desc in entries:
            rows.append((name, args, desc, cat_title))
    return rows


def resolve_json_path(name: str) -> pathlib.Path | None:
    filename = JSON_ALIASES.get(name, f"{name}.json")
    for base in (LOCAL_JSON_DIR, TEST_JSON_DIR):
        path = base / filename
        if path.is_file():
            return path
    return None


def load_sample_json(name: str) -> tuple[str | None, str | None]:
    path = resolve_json_path(name)
    if not path:
        return None, None
    raw = path.read_text(encoding="utf-8")
    try:
        pretty = json.dumps(json.loads(raw), indent=2, ensure_ascii=False)
    except json.JSONDecodeError:
        pretty = raw
    return path.name, pretty


def param_items(args: str) -> str:
    inner = args[1:-1] if args.startswith("(") and args.endswith(")") else args
    params = [p.strip() for p in inner.split(",") if p.strip()]
    if not params:
        return "<li>" + u("\\uc785\\ub825 \\ud30c\\ub77c\\ubbf8\\ud130\\uac00 \\uc5c6\\uc2b5\\ub2c8\\ub2e4.") + "</li>"
    return "".join("<li><code>" + html.escape(p) + "</code></li>" for p in params)


def sample_section(name: str) -> str:
    filename, pretty = load_sample_json(name)
    if not pretty:
        return (
            '          <li class="changelog-item">\n'
            '            <div class="changelog-meta">\n'
            '              <span class="changelog-version">'
            + u("\\uc0d8\\ud50c \\uc694\\uccad")
            + "</span>\n"
            "            </div>\n"
            "            <p>"
            + u("\\uc0d8\\ud50c JSON\\uc774 \\uc900\\ube44\\ub418\\uc9c0 \\uc54a\\uc558\\uc2b5\\ub2c8\\ub2e4.")
            + "</p>\n"
            "          </li>\n"
        )
    return (
        '          <li class="changelog-item">\n'
        '            <div class="changelog-meta">\n'
        '              <span class="changelog-version">'
        + u("\\uc0d8\\ud50c \\uc694\\uccad")
        + "</span>\n"
        "              <span>"
        + html.escape(filename or "")
        + "</span>\n"
        "            </div>\n"
        '            <pre class="func-json-sample">'
        + html.escape(pretty)
        + "</pre>\n"
        "          </li>\n"
    )


def page_html(name: str, args: str, desc: str, category_title: str) -> str:
    endpoint = "POST /xlfunction/" + name
    return (
        "<!DOCTYPE html>\n<html lang=\"ko\">\n<head>\n"
        "  <meta charset=\"UTF-8\">\n"
        "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
        '  <meta name="description" content="'
        + html.escape(name + " — PricingAPI XLFunction")
        + '">\n'
        "  <title>"
        + html.escape(name)
        + " | PricingAPI</title>\n"
        '  <link rel="stylesheet" href="../css/style.css">\n'
        "</head>\n<body>\n"
        '  <header class="site-header">\n'
        '    <div class="container header-inner">\n'
        '      <a class="logo" href="../index.html">\n'
        '        <span class="logo-name">QuantDev</span>\n'
        '        <span class="logo-tagline">Financial Engineering</span>\n'
        "      </a>\n"
        '      <div class="header-right">\n'
        "        <nav>\n"
        "          <ul>\n"
        '            <li><a href="../index.html">'
        + u("\\uc18c\\uac1c")
        + "</a></li>\n"
        '            <li><a href="../programs.html">Programs</a></li>\n'
        '            <li><a href="../portfolios.html">Portfolios</a></li>\n'
        '            <li><a href="../pricing-api.html" class="active">PricingAPI</a></li>\n'
        '            <li><a href="../contact.html">Contact</a></li>\n'
        "          </ul>\n"
        "        </nav>\n"
        '        <a class="btn btn-primary header-cta" href="../contact.html">'
        + u("\\ubb38\\uc758\\ud558\\uae30")
        + "</a>\n"
        "      </div>\n"
        "    </div>\n"
        "  </header>\n\n"
        "  <main>\n"
        '    <section class="page-hero program-updates-hero func-detail-hero">\n'
        '      <div class="container">\n'
        '        <p class="eyebrow">PricingAPI · '
        + html.escape(category_title)
        + "</p>\n"
        "        <h1>"
        + html.escape(name)
        + "</h1>\n"
        "        <div>"
        + sig_html(name, args)
        + "</div>\n"
        '        <a class="page-back" href="../pricing-api.html#functions">'
        + u("\\u2190 \\uc9c0\\uc6d0 \\ud568\\uc218 \\ubaa9\\ub85d\\uc73c\\ub85c")
        + "</a>\n"
        "      </div>\n"
        "    </section>\n\n"
        '    <section class="page-body">\n'
        '      <div class="container">\n'
        '        <div class="changelog-panel">\n'
        '          <ol class="changelog-list">\n'
        '            <li class="changelog-item">\n'
        '              <div class="changelog-meta">\n'
        '                <span class="changelog-version">'
        + u("\\uac1c\\uc694")
        + "</span>\n"
        "              </div>\n"
        "              <p>"
        + html.escape(desc)
        + "</p>\n"
        "            </li>\n"
        '            <li class="changelog-item">\n'
        '              <div class="changelog-meta">\n'
        '                <span class="changelog-version">'
        + u("\\uc785\\ub825 \\ud30c\\ub77c\\ubbf8\\ud130")
        + "</span>\n"
        "              </div>\n"
        "              <ul>\n"
        + param_items(args)
        + "              </ul>\n"
        "            </li>\n"
        '            <li class="changelog-item">\n'
        '              <div class="changelog-meta">\n'
        '                <span class="changelog-version">API</span>\n'
        "              </div>\n"
        "              <ul>\n"
        "<li><code>"
        + html.escape(endpoint)
        + "</code></li>\n"
        "<li>"
        + u("Excel Function\\u00b7C#\\u00b7Python \\ud074\\ub77c\\uc774\\uc5b8\\ud2b8\\uc5d0\\uc11c \\ub3d9\\uc77c\\ud55c \\ud568\\uc218\\uba85\\uc73c\\ub85c \\ud638\\ucd9c")
        + "</li>\n"
        "              </ul>\n"
        "            </li>\n"
        + sample_section(name)
        + "          </ol>\n"
        "        </div>\n"
        "      </div>\n"
        "    </section>\n"
        "  </main>\n\n"
        '  <footer class="site-footer">\n'
        '    <div class="container">\n'
        '      <div class="footer-grid">\n'
        '        <div class="footer-brand">\n'
        '          <div class="logo-name">QuantDev</div>\n'
        "          <p>"
        + u("\\uae08\\uc735\\uacf5\\ud559 \\ubc0f \\uac1c\\ubc1c \\uc11c\\ube44\\uc2a4\\ub97c \\uc81c\\uacf5\\ud558\\ub294 \\uac1c\\uc778 \\uc804\\ubb38\\uac00 \\ud3ec\\ud2b8\\ud3f4\\ub9ac\\uc624\\uc785\\ub2c8\\ub2e4.")
        + "</p>\n"
        "        </div>\n"
        '        <div class="footer-col">\n'
        "          <h4>Services</h4>\n"
        "          <ul>\n"
        '            <li><a href="../index.html">'
        + u("\\uc18c\\uac1c")
        + "</a></li>\n"
        '            <li><a href="../programs.html">Programs</a></li>\n'
        '            <li><a href="../pricing-api.html">PricingAPI</a></li>\n'
        "          </ul>\n"
        "        </div>\n"
        '        <div class="footer-col">\n'
        "          <h4>Contact</h4>\n"
        "          <ul>\n"
        '            <li><a href="../contact.html">'
        + u("\\ubb38\\uc758\\ud558\\uae30")
        + "</a></li>\n"
        '            <li><a href="../portfolios.html">Portfolios</a></li>\n'
        "          </ul>\n"
        "        </div>\n"
        "      </div>\n"
        '      <div class="footer-bottom">&copy; 2026 QuantDev. All rights reserved.</div>\n'
        "    </div>\n"
        "  </footer>\n"
        "</body>\n</html>\n"
    )


def build_catalog() -> str:
    cats = "".join(category(t, c, e) for t, c, e in DATA)
    return (
        '        <div class="section-header" id="functions">\n'
        '          <span class="section-label">Functions</span>\n'
        "          <h2>"
        + u("\\uc9c0\\uc6d0 \\ud568\\uc218 \\ubaa9\\ub85d")
        + "</h2>\n"
        "          <p>"
        + u("Excel Function \\u00b7 REST API \\u00b7 C# \\u00b7 Python\\uc5d0\\uc11c \\ub3d9\\uc77c\\ud55c \\ud568\\uc218\\uba85\\uc73c\\ub85c \\ud638\\ucd9c\\ud560 \\uc218 \\uc788\\uc2b5\\ub2c8\\ub2e4. \\uadf8\\ub8f9\\uc744 \\ud3bc\\uce58\\uba74 \\ud568\\uc218\\uba85\\u00b7\\uc785\\ub825 \\ud30c\\ub77c\\ubbf8\\ud130\\u00b7\\uc124\\uba85\\uc744 \\ud655\\uc778\\ud560 \\uc218 \\uc788\\uc2b5\\ub2c8\\ub2e4.")
        + "</p>\n"
        "        </div>\n"
        '        <div class="func-catalog" style="margin-bottom: 2.5rem;">\n'
        + cats
        + "        </div>\n\n"
    )


def generate_detail_pages() -> int:
    FUNC_DIR.mkdir(parents=True, exist_ok=True)
    SAMPLES_DIR.mkdir(parents=True, exist_ok=True)
    count = 0
    for name, args, desc, cat in iter_functions():
        out = FUNC_DIR / f"{name}.html"
        out.write_text(page_html(name, args, desc, cat), encoding="utf-8", newline="\n")
        src = resolve_json_path(name)
        if src:
            shutil.copy2(src, SAMPLES_DIR / src.name)
        count += 1
    return count


def patch_catalog() -> None:
    text = TARGET.read_text(encoding="utf-8")
    if MARKER not in text:
        raise SystemExit("insertion marker not found")
    if "func-catalog" in text:
        start = text.index('        <div class="section-header"')
        fn_idx = text.find('          <span class="section-label">Functions</span>', start)
        if fn_idx == -1:
            raise SystemExit("Functions section not found")
        start = text.rfind('        <div class="section-header"', 0, fn_idx)
        end = text.index(MARKER)
        text = text[:start] + build_catalog() + text[end:]
    else:
        text = text.replace(MARKER, build_catalog() + MARKER, 1)
    TARGET.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    pages = generate_detail_pages()
    patch_catalog()
    print(f"generated {pages} pages in {FUNC_DIR}")
    print(f"patched catalog in {TARGET}")


if __name__ == "__main__":
    main()
