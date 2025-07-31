import { Card } from 'primereact/card';
        
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
  
  const cardImage = (
    <img 
      src={imageUrl} 
      alt="Player card"
      className='small-card-image'
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