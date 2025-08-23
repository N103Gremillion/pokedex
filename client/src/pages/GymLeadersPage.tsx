import { useParams } from "react-router-dom";
import { Generation, getGenerationFromString } from "../types";
import { useEffect, useState } from "react";
import { sleep } from "../utils";

export const GymLeadersPage = () => {
  // pull of the genreatoin info from the url 
  const { generationString = "" } = useParams<{ generationString? : string }>();
  const [ loading, setLoading ] = useState<boolean>(false);

  // request the gymLeaders info from the backend every time a different generation is selected
  useEffect(() => {
    const run = async () => {
      setLoading(true);
      await sleep(2);

      // map the genrationString to the enum
      const generation : Generation = getGenerationFromString(generationString);
      
      // only make the fetch if the generatoin is not INVALID
      if (generation === Generation.INVALID) {
        setLoading(false)
        return
      }
      setLoading(false)
    };
    
    run();
  }, [generationString]);
  
  if (loading) { return <div className='loading-page'>Loading...</div>};

  return (
    <div className='general-page'>

      <h1 className='header'>Gym Leaders Page</h1>
      <p>This is the gym leaders page.</p>

    </div>
  );
}