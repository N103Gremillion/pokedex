import { CCard, CCardBody, CCardImage, CCardText, CCardTitle, CCardSubtitle, CCardLink } from '@coreui/react'

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
  link? : string;
}

export const InfoCard = ({size, title, subtitle, text, imageUrl, link} : InfoCardProps) => {
  

  return (
    <CCard className={`${size}-card`}>
      <CCardImage 
        orientation="top" 
        src={imageUrl} 
        alt=""
        style= {{
          width: '100%',
          height: '200px',
          objectFit: 'cover'
        }}
      />
      <CCardBody>
        <CCardTitle className='card-title'>{title}</CCardTitle>
        <CCardSubtitle className="mb-2 text-body-secondary">{subtitle}</CCardSubtitle>
        <CCardText className='card-text'>
          {text}
        </CCardText>
        <CCardLink href={link}>{link}</CCardLink>
      </CCardBody>
    </CCard>
  )
}