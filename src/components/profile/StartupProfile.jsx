import {
    FaBuilding,
    FaCalendarAlt,
    FaMoneyBillWave,
    FaUsers,
    FaMapMarkerAlt
} from "react-icons/fa";

import { useContext } from "react";
import { StartupContext } from "../context/StartupContext.jsx";
import { CurrencyContext } from "../context/CurrencyContext.jsx";
import { formatCurrency } from "../../utils/formatCurrency.js";


function StartupProfile() {

    const { startupData } = useContext(StartupContext);
    const { currency } = useContext(CurrencyContext);


    if (!startupData) {

        return (

            <div
                className="
                bg-white
                rounded-2xl
                shadow-md
                p-6
                mt-8
                text-gray-500
                "
            >

                Search a startup to view profile

            </div>

        );

    }


    const startup = startupData.startup;


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

            <div
                className="
                flex
                items-center
                gap-3
                mb-6
                "
            >

                <FaBuilding
                    className="
                    text-blue-600
                    text-3xl
                    "
                />

                <h2
                    className="
                    text-2xl
                    font-bold
                    "
                >
                    Startup Profile
                </h2>

            </div>



            <div
                className="
                grid
                grid-cols-1
                md:grid-cols-2
                xl:grid-cols-3
                gap-5
                "
            >


                <div
                    className="
                    bg-gray-50
                    rounded-xl
                    p-5
                    "
                >

                    <p
                        className="
                        text-gray-500
                        text-sm
                        "
                    >
                        Startup Name
                    </p>

                    <h3
                        className="
                        font-bold
                        text-lg
                        mt-1
                        "
                    >
                        {startup.Startup_Name}
                    </h3>

                </div>



                <div
                    className="
                    bg-gray-50
                    rounded-xl
                    p-5
                    "
                >

                    <p
                        className="
                        text-gray-500
                        text-sm
                        "
                    >
                        Sector
                    </p>

                    <h3
                        className="
                        font-bold
                        text-lg
                        mt-1
                        "
                    >
                        {startup.sector}
                    </h3>

                </div>



                <div
                    className="
                    bg-gray-50
                    rounded-xl
                    p-5
                    "
                >

                    <p
                        className="
                        text-gray-500
                        text-sm
                        flex
                        items-center
                        gap-2
                        "
                    >

                        <FaCalendarAlt />

                        Founded

                    </p>

                    <h3
                        className="
                        font-bold
                        text-lg
                        mt-1
                        "
                    >
                        {startup.founded_year}
                    </h3>

                </div>



                <div
                    className="
                    bg-gray-50
                    rounded-xl
                    p-5
                    "
                >

                    <p
                        className="
                        text-gray-500
                        text-sm
                        flex
                        items-center
                        gap-2
                        "
                    >

                        <FaMapMarkerAlt />

                        Headquarters

                    </p>

                    <h3
                        className="
                        font-bold
                        text-lg
                        mt-1
                        "
                    >
                        {startup.headquarters}
                    </h3>

                </div>



                <div
                    className="
                    bg-gray-50
                    rounded-xl
                    p-5
                    "
                >

                    <p
                        className="
                        text-gray-500
                        text-sm
                        flex
                        items-center
                        gap-2
                        "
                    >

                        <FaMoneyBillWave />

                        Total Funding

                    </p>

                    <h3
                        className="
                        font-bold
                        text-lg
                        mt-1
                        "
                    >
                        {formatCurrency(
                            startup.Total_Funding_Raised,
                            currency
                        )}
                    </h3>

                </div>



                <div
                    className="
                    bg-gray-50
                    rounded-xl
                    p-5
                    "
                >

                    <p
                        className="
                        text-gray-500
                        text-sm
                        flex
                        items-center
                        gap-2
                        "
                    >

                        <FaUsers />

                        Investors

                    </p>

                    <h3
                        className="
                        font-bold
                        text-lg
                        mt-1
                        break-words
                        "
                    >
                        {startup.Investors_List}
                    </h3>

                </div>


            </div>

        </div>

    );

}


export default StartupProfile;