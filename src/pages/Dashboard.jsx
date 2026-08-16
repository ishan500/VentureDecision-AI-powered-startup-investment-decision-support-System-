import KPICards from "../components/overview/KPICards";
import ChartsSection from "../components/charts/ChartsSection";

import StartupProfile from "../components/profile/StartupProfile";
import PredictionDashboard 
from "../components/predictions/PredictionDashboard";

const Dashboard =()=>{


return(

<div>


<h2 
className="
text-3xl
font-bold
"
>
Startup Intelligence Dashboard
</h2>


<p 
className="
text-gray-500
mt-2
"
>
AI powered startup evaluation and investment analysis
</p>



<KPICards/>


<ChartsSection/>

<StartupProfile/>
<PredictionDashboard/>

</div>

)

}


export default Dashboard;