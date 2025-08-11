// import { DataTable } from 'primereact/datatable';
// import { Column } from 'primereact/column';
// import { getTopConsolePlayers, getTopPcPlayers } from '../api/player-api';
// import { useEffect, useState } from 'react';
// import '../styles/general.css'

// export enum LeaderboardTypes {
//   Pc = 'pc',
//   Console = 'console'
// }

// interface LeaderboardProps {
//   platformType: LeaderboardTypes;
// }

// export type leaderboardPlayerData = {
//   name : string,
//   rank : R6rank,
//   region : PlayerRegion,
//   level : number,
//   kd : number,
//   profilePicUrl: string 
// }

// export const Leaderboard = ( {platformType} : LeaderboardProps) => {
  
//   const [playerData, setPlayerData] = useState<leaderboardPlayerData[]>([]);
//   const [loading, setLoading] = useState(true);

//   useEffect(() => {
//     const fetchData = async () => {
//       setLoading(true);
//       let data;

//       if (platformType === LeaderboardTypes.Pc) {
//         data = await getTopPcPlayers();
//       } else {
//         data = await getTopConsolePlayers();
//       }

//       setPlayerData(data);
//       setLoading(false);
//     };
//     fetchData(); // invoke 
//   }, [platformType]);

//   const getProfilePic = (rowData: leaderboardPlayerData) => {
//     return (
//       <img
//         src={rowData.profilePicUrl}
//         alt={rowData.name}
//         style={{
//           width: '40px',
//           height: '40px',
//           borderRadius: '50%',
//           objectFit: 'cover',
//         }}
//       />
//     );
//   };

//   const getRankBadge = (rowData: leaderboardPlayerData) => {
//     const badgeUrl = rankBadgeMap[rowData.rank];
//     return (
//       <img
//         src={badgeUrl}
//         alt={rowData.rank}
//         title={rowData.rank}  // optional: tooltip on hover
//         style={{
//           width: '40px',
//           height: '40px',
//           objectFit: 'contain',
//         }}
//       />
//     );
//   };

//   return (
//     <div>
//       <h2 className='header'>{platformType}</h2>
//       <DataTable 
//         value={playerData}
//         tableStyle={{ minWidth: '50rem' }}
//         className='leaderboard'
//         scrollHeight='400px'
//         stripedRows
//       > 
//         <Column header="Avatar" body={getProfilePic} style={{width: '60px'}} headerStyle={{ textAlign: 'center' }}/>
//         <Column field='name' header='Player Name' style={{ minWidth: '100px' }} headerStyle={{ textAlign: 'center' }}/>
//         <Column header='Rank' body={getRankBadge} style={{ minWidth: '100px'}} headerStyle={{ textAlign: 'center' }}/>
//         <Column field='region' header='Region' style={{ minWidth: '120px' }} headerStyle={{ textAlign: 'center' }}/>
//         <Column field='level' header='Level' style={{ minWidth: '80px' }} headerStyle={{ textAlign: 'center' }}/>
//         <Column field="kd" header='K/D' style={{ minWidth: '80px' }} headerStyle={{ textAlign: 'center' }}/>
//       </DataTable>
//     </div>
//   );
// }