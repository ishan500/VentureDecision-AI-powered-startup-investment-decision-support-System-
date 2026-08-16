import Sidebar from "./Sidebar";
import Navbar from "./Navbar";


const MainLayout = ({children}) => {


return (

<div>

<Sidebar/>


<div>

<Navbar/>


<main
className="
ml-72
p-8
bg-gray-50
min-h-screen
"
>

{children}

</main>


</div>


</div>

)


}


export default MainLayout;