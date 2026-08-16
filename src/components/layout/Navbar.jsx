import {
 UserCircle
} from "lucide-react";

import SearchBar from "../search/SearchBar";


const Navbar =()=>{


return(

<header
className="
h-20
bg-white
border-b
flex
items-center
justify-between
px-8
ml-72
"
>


<SearchBar />


<div className="
flex
items-center
gap-3
">

<UserCircle
size={35}
/>

<div>

<p className="font-semibold">
Investor
</p>

<p className="text-sm text-gray-500">
Premium Account
</p>

</div>


</div>


</header>

)


}


export default Navbar;