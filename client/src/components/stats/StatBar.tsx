import { ProgressBar } from 'primereact/progressbar';

interface StatBarProps {
  label : string;
  value : number;
  max : number;
  color : string
}

export const StatBar = ({label, value, max, color} : StatBarProps) => {
  const percentage : number = (value / max) * 100;

  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'space-between'}}>
        <span>{label}</span>
        <span>{value}</span>
      </div>
      <ProgressBar 
        value={percentage} 
        showValue={false} 
        style={{ height: '20px', width:'100%' }}
        className={`stat-bar-${label}`} 
      />
      <style>
        {`
          .stat-bar-${label} {
            background-color: #333;
          }
          .stat-bar-${label} .p-progressbar-value {
            background-color: ${color};
          }
        `}
      </style>
    </div>
  );
}