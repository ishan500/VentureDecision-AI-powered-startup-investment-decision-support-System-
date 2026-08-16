import { createContext, useState } from "react";


export const StartupContext = createContext();


export function StartupProvider({children}){


    const [startupData,setStartupData] = useState(null);


    return (

        <StartupContext.Provider
            value={{
                startupData,
                setStartupData
            }}
        >

            {children}

        </StartupContext.Provider>

    );

}