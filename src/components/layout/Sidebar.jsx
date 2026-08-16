import {
  LayoutDashboard,
  Search,
  BarChart3,
  FileText,
  Brain,
  Users
} from "lucide-react";


const Sidebar = () => {

  const menu = [
    {
      name:"Dashboard",
      icon:LayoutDashboard
    },
    {
      name:"Startup Explorer",
      icon:Search
    },
    {
      name:"Analytics",
      icon:BarChart3
    },
    {
      name:"Reports",
      icon:FileText
    },
    {
      name:"AI Copilot",
      icon:Brain
    },
    {
      name:"Investor Matching",
      icon:Users
    }
  ];


  return (

    <aside className="
      w-72
      h-screen
      bg-slate-950
      text-white
      fixed
      left-0
      top-0
      flex
      flex-col
      px-6
      py-8
    ">


      <h1 className="
        text-3xl
        font-bold
        text-blue-500
        mb-10
      ">
        VentureDecision
      </h1>


      <nav className="space-y-3">

      {
        menu.map((item,index)=>{

          const Icon=item.icon;

          return(
            <div
            key={index}
            className="
            flex
            items-center
            gap-4
            px-4
            py-3
            rounded-xl
            hover:bg-slate-800
            cursor-pointer
            transition
            "
            >

              <Icon size={20}/>

              <span>
                {item.name}
              </span>

            </div>
          )

        })
      }


      </nav>


    </aside>

  )

}


export default Sidebar;