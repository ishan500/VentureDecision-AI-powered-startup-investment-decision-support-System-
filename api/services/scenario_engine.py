# ==========================================================
# SCENARIO ENGINE
# VentureDecision
# ==========================================================


from typing import (

    Dict,

    Any,

    Optional

)


import copy


# ==========================================================
# SAFE NUMERIC CONVERSION
# ==========================================================

def to_float(

    value: Any,

    default: float = 0.0

) -> float:


    if value is None:

        return default


    try:

        return float(value)


    except (

        TypeError,

        ValueError

    ):

        return default


# ==========================================================
# ROUND VALUE
# ==========================================================

def round_value(

    value: Any,

    decimals: int = 2

):


    try:

        return round(

            float(value),

            decimals

        )


    except (

        TypeError,

        ValueError

    ):

        return value


# ==========================================================
# CHECK NUMERIC VALUE
# ==========================================================

def is_numeric(

    value: Any

) -> bool:


    if value is None:

        return False


    try:

        float(value)

        return True


    except (

        TypeError,

        ValueError

    ):

        return False


# ==========================================================
# METRICS WHERE HIGHER VALUE IS BETTER
# ==========================================================

HIGHER_IS_BETTER = {


    "Revenue",

    "Revenue_Growth_Percentage",

    "Gross_Margin",

    "Employee_Growth_Rate",

    "Website_Traffic",

    "Monthly_Active_Users",

    "Customer_Growth_Rate",

    "TAM",

    "Market_Size",

    "Market_Share",

    "Total_Funding_Raised",

    "Latest_Funding_Amount",

    "Overall_Startup_Score",

    "Financial_Health_Score",

    "Operational_Strength_Score",

    "Investor_Confidence_Score",

    "Growth_Score",

    "Market_Opportunity_Score",

    "Competitive_Strength_Score",

    "Funding_Score",

    "Popularity_Score",

    "Success_Probability",

    "Funding_Readiness_Score",

    "Acquisition_Probability",

    "IPO_Probability",

    "Exit_Probability",

    "Market_Leadership_Probability",

    "Competitive_Survival_Probability",

    "Valuation_Growth_Prediction",

    "Follow_On_Funding_Probability",

    "Investor_Match_Score",

    "Behavioral_Match_Score"


}


# ==========================================================
# METRICS WHERE LOWER VALUE IS BETTER
# ==========================================================

LOWER_IS_BETTER = {


    "Burn_Risk_Probability",

    "Failure_Probability",

    "Red_Flag_Count"


}


# ==========================================================
# CALCULATE METRIC DIFFERENCE
# ==========================================================

def calculate_metric_difference(

    baseline_value: Any,

    scenario_value: Any

) -> Dict[str, Any]:


    baseline = to_float(

        baseline_value

    )


    scenario = to_float(

        scenario_value

    )


    absolute_change = (

        scenario - baseline

    )


    percentage_change = None


    if baseline != 0:


        percentage_change = (

            absolute_change

            /

            abs(baseline)

        ) * 100


    return {


        "baseline": round_value(

            baseline

        ),


        "scenario": round_value(

            scenario

        ),


        "absolute_change": round_value(

            absolute_change

        ),


        "percentage_change": (

            round_value(

                percentage_change

            )

            if percentage_change is not None

            else None

        )


    }


# ==========================================================
# DETERMINE METRIC IMPACT
# ==========================================================

def determine_impact(

    metric: str,

    change: float

) -> str:


    if abs(change) < 0.0001:

        return "unchanged"


    if metric in HIGHER_IS_BETTER:


        if change > 0:

            return "positive"


        return "negative"


    if metric in LOWER_IS_BETTER:


        if change < 0:

            return "positive"


        return "negative"


    return "changed"


# ==========================================================
# APPLY SCENARIO CHANGES
# ==========================================================

def apply_scenario_changes(

    startup: Dict[str, Any],

    scenario_changes: Dict[str, Any]

) -> Dict[str, Any]:


    scenario_startup = copy.deepcopy(

        startup

    )


    for metric, new_value in (

        scenario_changes.items()

    ):


        if metric not in scenario_startup:

            continue


        scenario_startup[metric] = (

            new_value

        )


    return scenario_startup


# ==========================================================
# COMPARE STARTUP STATES
# ==========================================================

def compare_startup_states(

    baseline_startup: Dict[str, Any],

    scenario_startup: Dict[str, Any]

) -> Dict[str, Any]:


    comparison = {}


    all_metrics = set(

        baseline_startup.keys()

    ).union(

        scenario_startup.keys()

    )


    for metric in all_metrics:


        baseline_value = (

            baseline_startup.get(

                metric

            )

        )


        scenario_value = (

            scenario_startup.get(

                metric

            )

        )


        # ==================================================
        # ONLY COMPARE NUMERIC VALUES
        # ==================================================

        if not is_numeric(

            baseline_value

        ):

            continue


        if not is_numeric(

            scenario_value

        ):

            continue


        # ==================================================
        # CALCULATE DIFFERENCE
        # ==================================================

        difference = (

            calculate_metric_difference(

                baseline_value,

                scenario_value

            )

        )


        # ==================================================
        # DETERMINE IMPACT
        # ==================================================

        impact = determine_impact(

            metric,

            difference[

                "absolute_change"

            ]

        )


        comparison[metric] = {


            **difference,


            "impact": impact


        }


    return comparison


# ==========================================================
# RUN SCENARIO
# ==========================================================

def run_scenario(

    startup: Dict[str, Any],

    scenario_changes: Dict[str, Any],

    scenario_name: Optional[str] = None

) -> Dict[str, Any]:


    # ======================================================
    # BASELINE STARTUP
    # ======================================================

    baseline_startup = copy.deepcopy(

        startup

    )


    # ======================================================
    # APPLY SCENARIO CHANGES
    # ======================================================

    scenario_startup = (

        apply_scenario_changes(

            startup,

            scenario_changes

        )

    )


    # ======================================================
    # COMPARE STARTUP STATES
    # ======================================================

    comparison = (

        compare_startup_states(

            baseline_startup,

            scenario_startup

        )

    )


    # ======================================================
    # CLASSIFY CHANGES
    # ======================================================

    positive_changes = {}


    negative_changes = {}


    unchanged_metrics = {}


    changed_metrics = {}


    for metric, result in (

        comparison.items()

    ):


        if result["impact"] == "positive":


            positive_changes[

                metric

            ] = result


        elif result["impact"] == "negative":


            negative_changes[

                metric

            ] = result


        elif result["impact"] == "unchanged":


            unchanged_metrics[

                metric

            ] = result


        else:


            changed_metrics[

                metric

            ] = result


    # ======================================================
    # FINAL SCENARIO RESULT
    # ======================================================

    return {


        "scenario_name": (

            scenario_name

        ),


        "scenario_changes": (

            scenario_changes

        ),


        "original_values": (

            baseline_startup

        ),


        "scenario_values": (

            scenario_startup

        ),


        "comparison": (

            comparison

        ),


        "positive_changes": (

            positive_changes

        ),


        "negative_changes": (

            negative_changes

        ),


        "unchanged_metrics": (

            unchanged_metrics

        ),


        "changed_metrics": (

            changed_metrics

        ),


        "summary": {


            "total_metrics_compared": (

                len(

                    comparison

                )

            ),


            "positive_change_count": (

                len(

                    positive_changes

                )

            ),


            "negative_change_count": (

                len(

                    negative_changes

                )

            ),


            "unchanged_metric_count": (

                len(

                    unchanged_metrics

                )

            )


        }


    }