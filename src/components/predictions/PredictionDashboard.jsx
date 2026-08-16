import {
    FaChartLine,
    FaExclamationTriangle,
    FaMoneyBillWave,
    FaRocket
} from "react-icons/fa";

import { useContext } from "react";
import { StartupContext } from "../context/StartupContext.jsx";


function PredictionDashboard() {

    const { startupData } = useContext(StartupContext);


    if (!startupData) {

        return (

            <div
                className="
                bg-white
                rounded-2xl
                shadow-md
                p-6
                mt-8
                text-center
                text-gray-500
                "
            >

                Search a startup to view prediction analysis.

            </div>

        );

    }


    const startup = startupData.startup;


    const getRiskColor = (risk) => {

        if (!risk) return "bg-gray-100 text-gray-700";

        switch (risk.toLowerCase()) {

            case "low":
                return "bg-green-100 text-green-700";

            case "medium":
                return "bg-yellow-100 text-yellow-700";

            case "high":
                return "bg-red-100 text-red-700";

            default:
                return "bg-gray-100 text-gray-700";
        }

    };


    const predictions = [

        {
            title: "Success Probability",
            value: `${startup.Success_Probability}%`,
            icon: FaChartLine
        },

        {
            title: "Risk Score",
            value: startup.Risk_Label,
            icon: FaExclamationTriangle
        },

        {
            title: "Funding Readiness",
            value: `${startup.Funding_Readiness_Confidence}%`,
            icon: FaMoneyBillWave
        },

        {
            title: "Acquisition Probability",
            value: `${startup.Acquisition_Probability}%`,
            icon: FaRocket
        }

    ];


    return (

        <div
            className="
            bg-white
            rounded-2xl
            shadow-md
            p-6
            mt-8
            "
        >

            <h2
                className="
                text-2xl
                font-bold
                mb-6
                "
            >
                ML Prediction Analysis
            </h2>


            <div
                className="
                grid
                grid-cols-1
                md:grid-cols-2
                xl:grid-cols-4
                gap-6
                "
            >

                {

                    predictions.map((item, index) => {

                        const Icon = item.icon;

                        return (

                            <div
                                key={index}
                                className="
                                bg-gray-50
                                rounded-xl
                                p-5
                                "
                            >

                                <div
                                    className="
                                    flex
                                    justify-between
                                    items-center
                                    "
                                >

                                    <div>

                                        <p
                                            className="
                                            text-gray-500
                                            text-sm
                                            "
                                        >
                                            {item.title}
                                        </p>

                                        {

                                            item.title === "Risk Score" ? (

                                                <span
                                                    className={`
                                                        mt-2
                                                        inline-block
                                                        px-3
                                                        py-1
                                                        rounded-full
                                                        text-sm
                                                        font-semibold
                                                        ${getRiskColor(item.value)}
                                                    `}
                                                >
                                                    {item.value}
                                                </span>

                                            ) : (

                                                <h3
                                                    className="
                                                    text-3xl
                                                    font-bold
                                                    mt-2
                                                    "
                                                >
                                                    {item.value}
                                                </h3>

                                            )

                                        }

                                    </div>


                                    <Icon
                                        className="
                                        text-blue-600
                                        text-3xl
                                        "
                                    />

                                </div>

                            </div>

                        );

                    })

                }

            </div>

        </div>

    );

}


export default PredictionDashboard;