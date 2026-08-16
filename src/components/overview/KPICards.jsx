import {
    FaChartLine,
    FaCheckCircle,
    FaExclamationTriangle,
    FaMoneyBillWave
} from "react-icons/fa";

import { useContext } from "react";
import { StartupContext } from "../context/StartupContext.jsx";


function KPICards() {

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

                Search a startup to view KPI metrics.

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


    const cards = [

        {
            title: "Startup Score",
            value: startup.Overall_Startup_Score,
            description: "Overall startup evaluation",
            icon: <FaChartLine />,
            color: "text-blue-600"
        },

        {
            title: "Success Probability",
            value: `${startup.Success_Probability}%`,
            description: "Probability of startup success",
            icon: <FaCheckCircle />,
            color: "text-green-600"
        },

        {
            title: "Risk Score",
            value: startup.Risk_Label,
            description: "Investment risk assessment",
            icon: <FaExclamationTriangle />,
            color: "text-red-600"
        },

        {
            title: "Funding Readiness",
            value: startup.Funding_Readiness_Score,
            description: startup.Funding_Readiness_Name,
            icon: <FaMoneyBillWave />,
            color: "text-purple-600"
        }

    ];


    return (

        <div
            className="
            grid
            grid-cols-1
            md:grid-cols-2
            xl:grid-cols-4
            gap-6
            mt-8
            "
        >

            {

                cards.map((card, index) => (

                    <div
                        key={index}
                        className="
                        bg-white
                        rounded-2xl
                        shadow-md
                        p-6
                        hover:shadow-xl
                        transition
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
                                    {card.title}
                                </p>

                                {

                                    card.title === "Risk Score" ? (

                                        <span
                                            className={`
                                                mt-2
                                                inline-block
                                                px-3
                                                py-1
                                                rounded-full
                                                text-sm
                                                font-semibold
                                                ${getRiskColor(card.value)}
                                            `}
                                        >
                                            {card.value}
                                        </span>

                                    ) : (

                                        <h2
                                            className="
                                            text-3xl
                                            font-bold
                                            mt-2
                                            "
                                        >
                                            {card.value}
                                        </h2>

                                    )

                                }

                                <p
                                    className="
                                    text-gray-400
                                    text-sm
                                    mt-2
                                    "
                                >
                                    {card.description}
                                </p>

                            </div>


                            <div
                                className={`
                                    text-3xl
                                    ${card.color}
                                `}
                            >
                                {card.icon}
                            </div>

                        </div>

                    </div>

                ))

            }

        </div>

    );

}


export default KPICards;