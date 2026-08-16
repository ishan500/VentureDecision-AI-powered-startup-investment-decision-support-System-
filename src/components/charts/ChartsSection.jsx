import BarChart from "./BarChart";
import DonutChart from "./DonutChart";
import RadarChart from "./RadarChart";
import ScatterChart from "./ScatterChart";


function ChartsSection() {

    return (

        <div
            className="
            grid
            grid-cols-1
            xl:grid-cols-2
            gap-6
            mt-8
            "
        >

            {/* Funding Overview */}

            <div
                className="
                bg-white
                rounded-2xl
                shadow-md
                p-6
                "
            >

                <h3
                    className="
                    text-xl
                    font-semibold
                    mb-4
                    "
                >
                    Funding Overview
                </h3>

                <BarChart />

            </div>


            {/* Risk Distribution */}

            <div
                className="
                bg-white
                rounded-2xl
                shadow-md
                p-6
                "
            >

                <h3
                    className="
                    text-xl
                    font-semibold
                    mb-4
                    "
                >
                    Risk Distribution
                </h3>

                <DonutChart />

            </div>


            {/* Startup Intelligence */}

            <div
                className="
                bg-white
                rounded-2xl
                shadow-md
                p-6
                "
            >

                <h3
                    className="
                    text-xl
                    font-semibold
                    mb-4
                    "
                >
                    Startup Intelligence Score
                </h3>

                <RadarChart />

            </div>


            {/* Growth vs Risk */}

            <div
                className="
                bg-white
                rounded-2xl
                shadow-md
                p-6
                "
            >

                <h3
                    className="
                    text-xl
                    font-semibold
                    mb-4
                    "
                >
                    Growth vs Risk Analysis
                </h3>

                <ScatterChart />

            </div>

        </div>

    );

}

export default ChartsSection;