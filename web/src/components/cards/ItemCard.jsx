import { DiscAlbum, User, Music, AudioLines } from "lucide-react";

function ItemCard({ cardClass, data, unit }) {
  const iconMap = {
    albums: DiscAlbum,
    artists: User,
    genres: Music,
    titles: AudioLines,
  };

  const IconComponent = iconMap[unit];

  if (!data) return <div className={cardClass}>No Data</div>;

  return (
    <div className={`${cardClass} flex flex-col items-center text-center gap-1`}>
      <div className="p-5 rounded-full bg-primary/20 text-primary mb-5">
        <IconComponent size={48} color="#4f46e5" />
      </div>
		  <span className="text-4xl font-semibold">
        {data.toLocaleString("fr-FR")}
      </span>
		  <span className="text-lg font-medium text-gray-500">
        {unit}
      </span>
    </div>
  );
}

export default ItemCard;
