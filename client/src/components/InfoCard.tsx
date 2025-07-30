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
  links? : string[];
}

export const InfoCard = ({size, title, subtitle, text, imageUrl, links} : InfoCardProps) => {


  return (
    <CCard className='small-card'>
      <CCardImage orientation="top" src="https://via.placeholder.com/300x150" alt="Card image" />
      <CCardBody>
        <CCardTitle>Card title</CCardTitle>
        <CCardSubtitle className="mb-2 text-body-secondary">Card subtitle</CCardSubtitle>
        <CCardText>
          Some quick example text to build on the card title and make up the bulk of the card's
          content.
        </CCardText>
        <CCardLink href="#">Card link</CCardLink>
        <CCardLink href="#">Another link</CCardLink>
      </CCardBody>
    </CCard>
  )
}