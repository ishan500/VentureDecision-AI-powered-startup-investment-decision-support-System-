import {
    BarChart as RechartsBarChart,
    Bar,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    ResponsiveContainer
} from "recharts";

import { useContext } from "react";
import { StartupContext } from "../context/StartupContext.jsx";


function BarChart() {

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

                Search a startup to view funding overview.

            </div>

        );

    }


    const startup = startupData.startup;


    const data = [

        {
            metric: "Total Funding",
            value: Number(startup.Total_Funding_Raised)
        },

        {
            metric: "Latest Funding",
            value: Number(startup.Latest_Funding_Amount)
        },

        {
            metric: "Funding Rounds",
            value: Number(startup.Number_of_Funding_Rounds)
        }

    ];


    return (

        <ResponsiveContainer
            width="100%"
            height={300}
        >

            <RechartsBarChart data={data}>

                <CartesianGrid strokeDasharray="3 3" />

                <XAxis dataKey="metric" />

                <YAxis />

                <Tooltip />

                <Bar
                    dataKey="value"
                    radius={[6, 6, 0, 0]}
                />

            </RechartsBarChart>

        </ResponsiveContainer>

    );

}


export default BarChart;