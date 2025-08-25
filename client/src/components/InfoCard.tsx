import { Card } from 'primereact/card';
import type { SyntheticEvent } from 'react';
        
// TODO : change to use primereact
export enum CardSize {
  small = 'small',
  medium = 'medium',
  large = 'large'
}

interface InfoCardProps {
  size : CardSize;
  title : string;
  subtitle? : string[];
  text : string;
  imageUrl? : string;
}

export const InfoCard = ({size, title, subtitle, text, imageUrl} : InfoCardProps) => {
  
  const defaultImageUrl : string = "/public/default_img.png";

  // construct the handler for when the image doesnt load
  const handleImageNotFound = (event : SyntheticEvent<HTMLImageElement, Event>) => {
    const img = event.currentTarget;
    img.src = defaultImageUrl;
  }

  const cardImage = (
    <img 
      src={imageUrl || defaultImageUrl} 
      alt="Player card"
      className='small-card-image'
      onError= {(error) => handleImageNotFound(error)}
    />
  );

  return (
    <Card
      header={cardImage}
      className={`${size}-card`} 
      title={<span className='small-card-title'>{title}</span>} 
      subTitle={subtitle}>
      <p className='small-card-text'>{text}</p>
    </Card>
  )
}