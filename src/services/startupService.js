const API_URL = "http://127.0.0.1:8000";


export const getStartup = async(startupName)=>{


    let startupData = null;
    let datasetType = null;



    // ----------------------------
    // Check New Dataset
    // ----------------------------

    try{

        const newResponse = await fetch(
            `${API_URL}/startups/new/${startupName}`
        );


        if(newResponse.ok){

            startupData = await newResponse.json();

            datasetType = "new";

        }


    }
    catch(error){

        console.log(
            "New dataset search failed"
        );

    }





    // ----------------------------
    // Check Old Dataset
    // ----------------------------

    if(!startupData){

        try{


            const oldResponse = await fetch(
                `${API_URL}/startups/old/${startupName}`
            );


            if(oldResponse.ok){

                startupData = await oldResponse.json();

                datasetType = "old";

            }


        }
        catch(error){

            console.log(
                "Old dataset search failed"
            );

        }

    }





    if(!startupData){

        throw new Error(
            "Startup not found"
        );

    }





    // ----------------------------
    // Return Startup Data Only
    // ----------------------------

    return {


        ...startupData,


        dataset_type: datasetType


    };


};