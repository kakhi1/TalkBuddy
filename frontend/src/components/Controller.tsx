import { useState } from "react"
import Title from "./Title";

const Controller = () => {
  const [isLoading,setIsLoading ] = useState(false);
  const [messages,setMessages ] = useState<any[]>([]);

  const createBlobUrl = (data:any) => {};

  const handlestop = async () =>{};

  return (
    <div className="h-screen overflow-y-hidden">
      <Title setMessages={setMessages}/>
      <div className="flex flex-col justify-between h-full overflow-y-hidden pb-96">
        Placeholder

      </div>
    </div>
  )
}

export default Controller