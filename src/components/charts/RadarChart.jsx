import {

    RadarChart as RechartsRadarChart,

    PolarGrid,

    PolarAngleAxis,

    PolarRadiusAxis,

    Radar,

    ResponsiveContainer,

    Tooltip

} from "recharts";

import { useContext } from "react";
import { StartupContext } from "../context/StartupContext.jsx";


function RadarChart() {

    const { startupData } = useContext(StartupContext);


    if (!startupData) {

        return (

            <div
                className="
                h-[300px]
                flex
                items-center
                justify-center
                text-gray-500
                "
            >

                Search a startup to view intelligence score.

            </div>

        );

    }


    const startup = startupData.startup;


    const data = [

        {
            metric: "Funding",
            score: Number(startup.Funding_Score)
        },

        {
            metric: "Financial",
            score: Number(startup.Financial_Health_Score)
        },

        {
            metric: "Growth",
            score: Number(startup.Growth_Score)
        },

        {
            metric: "Market",
            score: Number(startup.Market_Opportunity_Score)
        },

        {
            metric: "Media",
            score: Number(startup.Media_Buzz_Score)
        },

        {
            metric: "Overall",
            score: Number(startup.Overall_Startup_Score)
        }

    ];


    return (

        <ResponsiveContainer
            width="100%"
            height={300}
        >

            <RechartsRadarChart data={data}>

                <PolarGrid />

                <PolarAngleAxis
                    dataKey="metric"
                />

                <PolarRadiusAxis
                    domain={[0, 100]}
                />

                <Radar
                    dataKey="score"
                />

                <Tooltip />

            </RechartsRadarChart>

        </ResponsiveContainer>

    );

}


export default RadarChart;