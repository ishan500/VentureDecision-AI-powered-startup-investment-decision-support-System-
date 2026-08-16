import {

    ScatterChart as RechartsScatterChart,

    Scatter,

    XAxis,

    YAxis,

    CartesianGrid,

    Tooltip,

    ResponsiveContainer

} from "recharts";

import { useContext } from "react";
import { StartupContext } from "../context/StartupContext.jsx";


function ScatterChart() {

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

                Search a startup to view Growth vs Risk Analysis.

            </div>

        );

    }


    const startup = startupData.startup;


    const data = [

        {
            growth: Number(startup.Growth_Score),
            risk: Number(startup.Burn_Risk_Score)
        }

    ];


    return (

        <ResponsiveContainer
            width="100%"
            height={300}
        >

            <RechartsScatterChart>

                <CartesianGrid />

                <XAxis
                    type="number"
                    dataKey="growth"
                    name="Growth Score"
                    domain={[0, 100]}
                />

                <YAxis
                    type="number"
                    dataKey="risk"
                    name="Burn Risk Score"
                    domain={[0, 100]}
                />

                <Tooltip
                    cursor={{ strokeDasharray: "3 3" }}
                />

                <Scatter
                    data={data}
                />

            </RechartsScatterChart>

        </ResponsiveContainer>

    );

}


export default ScatterChart;