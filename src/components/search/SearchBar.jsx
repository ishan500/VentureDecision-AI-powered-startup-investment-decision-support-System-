import { useState, useContext } from "react";
import { Search } from "lucide-react";

import { getStartup } from "../../services/startupService";
import { StartupContext } from "../context/StartupContext.jsx";


function SearchBar() {

    const [startup, setStartup] = useState("");

    const { setStartupData } = useContext(StartupContext);



    const handleSearch = async () => {

        if (!startup.trim()) return;


        try {

            const data = await getStartup(startup);


            console.log("Startup Data:", data);

            // Add these temporary debug lines
            console.log(Object.keys(data.startup));
            console.table(data.startup);


            // Store startup data globally
            setStartupData(data);


        } catch (error) {

            console.log(
                "Error:",
                error.message
            );

        }

    };



    return (

        <div
            className="
            flex
            items-center
            gap-3
            bg-gray-100
            rounded-xl
            px-4
            py-2
            w-full
            "
        >

            <Search size={20} />


            <input

                type="text"

                placeholder="Search startups..."

                value={startup}

                onChange={(e) => setStartup(e.target.value)}


                onKeyDown={(e) => {

                    if (e.key === "Enter") {

                        handleSearch();

                    }

                }}


                className="
                bg-transparent
                outline-none
                w-full
                "

            />



            <button

                onClick={handleSearch}

                className="
                bg-blue-600
                text-white
                px-4
                py-2
                rounded-lg
                hover:bg-blue-700
                transition
                "

            >

                Search

            </button>


        </div>

    );

}


export default SearchBar;