import { useContext } from "react";
import { CurrencyContext } from "../../context/CurrencyContext.jsx";


function CurrencyToggle() {

    const {
        currency,
        setCurrency
    } = useContext(CurrencyContext);


    return (

        <div
            className="
            flex
            items-center
            bg-gray-100
            rounded-lg
            p-1
            "
        >

            <button

                onClick={() => setCurrency("USD")}

                className={`
                    px-4
                    py-2
                    rounded-md
                    text-sm
                    font-medium
                    transition
                    ${
                        currency === "USD"
                            ? "bg-blue-600 text-white"
                            : "text-gray-600 hover:bg-gray-200"
                    }
                `}
            >

                USD

            </button>


            <button

                onClick={() => setCurrency("INR")}

                className={`
                    px-4
                    py-2
                    rounded-md
                    text-sm
                    font-medium
                    transition
                    ${
                        currency === "INR"
                            ? "bg-blue-600 text-white"
                            : "text-gray-600 hover:bg-gray-200"
                    }
                `}
            >

                INR (Cr)

            </button>

        </div>

    );

}


export default CurrencyToggle;