import {
    PieChart,
    Pie,
    Cell,
    Tooltip,
    ResponsiveContainer,
    Legend
} from "recharts";

import { useContext } from "react";
import { StartupContext } from "../context/StartupContext.jsx";


function DonutChart() {

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

                Search a startup to view risk distribution.

            </div>

        );

    }


    const startup = startupData.startup;


    const data = [

        {
            name: "Burn Risk",
            value: Number(startup.Burn_Risk_Score)
        },

        {
            name: "Financial Health",
            value: Number(startup.Financial_Health_Score)
        },

        {
            name: "Operational Strength",
            value: Number(startup.Operational_Strength_Score)
        },

        {
            name: "Competitive Strength",
            value: Number(startup.Competitive_Strength_Score)
        }

    ];


    const COLORS = [

        "#ef4444",
        "#22c55e",
        "#3b82f6",
        "#a855f7"

    ];


    return (

        <ResponsiveContainer
            width="100%"
            height={300}
        >

            <PieChart>

                <Pie

                    data={data}

                    dataKey="value"

                    nameKey="name"

                    cx="50%"

                    cy="50%"

                    innerRadius={70}

                    outerRadius={100}

                    paddingAngle={3}

                >

                    {

                        data.map((entry, index) => (

                            <Cell
                                key={index}
                                fill={COLORS[index % COLORS.length]}
                            />

                        ))

                    }

                </Pie>

                <Tooltip />

                <Legend />

            </PieChart>

        </ResponsiveContainer>

    );

}


export default DonutChart;