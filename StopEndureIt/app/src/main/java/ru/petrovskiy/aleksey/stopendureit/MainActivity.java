package ru.petrovskiy.aleksey.stopendureit;

import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.os.Environment;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.widget.ImageView;
import android.widget.TextView;

import com.bumptech.glide.Glide;
import com.bumptech.glide.load.engine.DiskCacheStrategy;
import com.bumptech.glide.request.RequestOptions;
import com.bumptech.glide.request.target.SimpleTarget;
import com.bumptech.glide.request.transition.Transition;
import com.googlecode.tesseract.android.TessBaseAPI;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = MainActivity.class.getSimpleName();
    private static final String DATA_PATH = Environment.getExternalStorageDirectory().toString() + "/StopEndureIt/";
    TessBaseAPI tessBaseAPI;
    private ImageView mImageViewDungeon;
    private TextView mTextView;
    private Bitmap theBitmap;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mImageViewDungeon = findViewById(R.id.imageViewDungeon);
        mTextView = findViewById(R.id.textView);

        createNotificationChannel();
        downloadPic();
    }

    private void createNotificationChannel() {
        NotificationManager mNotificationManager = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) {
            NotificationChannel mChannel = new NotificationChannel(Constants.CHANNEL_ID, Constants.CHANNEL_NAME, NotificationManager.IMPORTANCE_HIGH);

            mChannel.setDescription(Constants.CHANNEL_DESCRIPTON);
            mChannel.enableLights(true);
            mChannel.setLightColor(R.color.colorRed);
            mChannel.enableVibration(true);

            mChannel.setVibrationPattern(new long[]{100, 200, 300, 400, 500, 400, 300, 200, 400});

            if (mNotificationManager != null) {
                mNotificationManager.createNotificationChannel(mChannel);
            }
        }
    }


    public void downloadPic() {
        String urlImage = "https://firebasestorage.googleapis.com/v0/b/dungeonhelperwow.appspot.com/o/dims.jpg?alt=media&token=f3a59b05-9ed9-43cf-88f9-25ce45b08d72";


//        Picasso.get()
//                .load(urlImage)
//                .memoryPolicy(MemoryPolicy.NO_CACHE)
//                .into(mImageViewDungeon);

//
//        RequestListener listener = new RequestListener() {
//            @Override
//            public boolean onLoadFailed(@Nullable GlideException e, Object model, Target target, boolean isFirstResource) {
//                return false;
//            }
//
//            @Override
//            public boolean onResourceReady(Object resource, Object model, Target target, DataSource dataSource, boolean isFirstResource) {
//                Bitmap bitmap = ((BitmapDrawable) mImageViewDungeon.getDrawable()).getBitmap();
//                return true;
//            }
//        };
//        Glide.with(this).asDrawable().load(urlImage).into(mImageViewDungeon);

        RequestOptions requestOptions = new RequestOptions()
                .diskCacheStrategy(DiskCacheStrategy.NONE)
                .skipMemoryCache(true);

        Glide.with(this)
                .asBitmap()
                .load(urlImage)
                .apply(requestOptions)
                .into(new SimpleTarget<Bitmap>() {
                    @Override
                    public void onResourceReady(@NonNull Bitmap resource, Transition<? super Bitmap> transition) {
//                        theBitmap = resource;
//                        mTextView.setText(getText(theBitmap));
                        mImageViewDungeon.setImageBitmap(resource);
                    }
                });
    }


//    public void StringToBitMap(String encodedString){
//        try{
//            byte [] encodeByte=Base64.decode(encodedString, Base64.DEFAULT);
//            Bitmap bitmap=BitmapFactory.decodeByteArray(encodeByte, 0, encodeByte.length);
//            getText(bitmap);
//        }catch(Exception e){
//            e.getMessage();
//        }
//    }


    //Thread executor to usage
//    public Bitmap getIconFromServer(final String name) {
//        final Bitmap[] bitmap = new Bitmap[1];
//        new Thread(new Runnable() {
//            @Override
//            public void run() {
////                bitmap[0] = Bitmap.createBitmap(Bitmap.Config.ALPHA_8);
//                FutureTarget<Bitmap> futureTarget =
//                        Glide.with(MainActivity.this)
//                                .asBitmap()
//                                .load(name)
//                                .submit();
//                try {
//                    bitmap[0] = futureTarget.get();
//                } catch (InterruptedException e) {
//                    e.printStackTrace();
//                } catch (ExecutionException e) {
//                    e.printStackTrace();
//                }
//            }
//        }).start();
//        try {
//            Thread.sleep(2000);
//            return bitmap[0];
//        } catch (InterruptedException e) {
//            e.printStackTrace();
//            return bitmap[0];
//        }
//    }

    private String getText(Bitmap bitmap) {
        try {
            tessBaseAPI = new TessBaseAPI();
        } catch (Exception e) {
            Log.e(TAG, e.getMessage());
        }
        tessBaseAPI.init(DATA_PATH, "eng");
        tessBaseAPI.setImage(bitmap);
        String retStr = "No result";
        try {
            retStr = tessBaseAPI.getUTF8Text();
        } catch (Exception e) {
            Log.e(TAG, e.getMessage());
        }
        tessBaseAPI.end();
        return retStr;
    }
}